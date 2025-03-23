import os
import subprocess
import time

# ASCII Art for "Vaishal"
ASCII_ART = """
██    ██  █████  ██  ██  ██████  ██   ██  █████  ██      
██    ██ ██   ██ ██  ██ ██       ██   ██ ██   ██ ██      
██    ██ ███████ █████  ██   ███ ███████ ███████ ██      
 ██  ██  ██   ██ ██  ██ ██    ██ ██   ██ ██   ██ ██      
  ████   ██   ██ ██  ██  ██████  ██   ██ ██   ██ ███████ 
"""

# Function to run Git commands
def run_git_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Error: {result.stderr.strip()}")
        return result.stdout.strip()
    except Exception as e:
        print(f"❌ Exception: {e}")

# Get unstaged files
def get_unstaged_files():
    output = run_git_command("git ls-files --others --exclude-standard")  # Get untracked files
    output2 = run_git_command("git diff --name-only")  # Get modified files
    files = output.split("\n") + output2.split("\n")
    return [file.strip() for file in files if file.strip()]

# Main function
def batch_commit():
    print(ASCII_ART)  # Display ASCII art
    print("🚀 Welcome to Vaishal's Git Commit Tool!\n")

    if not os.path.exists(".git"):
        print("⚠️  This is not a Git repository! Initializing Git...")
        run_git_command("git init")

    while True:
        files = get_unstaged_files()
        if not files:
            print("✅ No unstaged files found!")
            break

        print(f"\n📂 Total unstaged files: {len(files)}")
        try:
            num = int(input("📌 How many files do you want to stage in this batch? (0 to exit): "))
            if num == 0:
                break
        except ValueError:
            print("❌ Invalid input. Enter a number!")
            continue

        batch = files[:num]
        print(f"\n✅ Staging {len(batch)} files...")
        run_git_command(f"git add {' '.join(batch)}")

        commit_msg = input("📝 Enter commit message: ") or "Batch commit"
        run_git_command(f'git commit -m "{commit_msg}"')

        push_choice = input("📤 Push changes to remote? (y/n): ").strip().lower()
        if push_choice == "y":
            run_git_command("git push")

        print("✅ Batch commit complete!\n")

    print("🎉 All files committed successfully!")

if __name__ == "__main__":
    batch_commit()

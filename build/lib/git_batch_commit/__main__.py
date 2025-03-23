import os
import subprocess

# ASCII Art for "Vaishal"
ASCII_ART = r"""
 ________      ___    ___      ___      ___ ________  ___  ________  ___  ___  ________  ___          
|\   __  \    |\  \  /  /|    |\  \    /  /|\   __  \|\  \|\   ____\|\  \|\  \|\   __  \|\  \         
\ \  \|\ /_   \ \  \/  / /    \ \  \  /  / | \  \|\  \ \  \ \  \___|\ \  \\\  \ \  \|\  \ \  \        
 \ \   __  \   \ \    / /      \ \  \/  / / \ \   __  \ \  \ \_____  \ \   __  \ \   __  \ \  \       
  \ \  \|\  \   \/  /  /        \ \    / /   \ \  \ \  \ \  \|____|\  \ \  \ \  \ \  \ \  \ \  \____  
   \ \_______\__/  / /           \ \__/ /     \ \__\ \__\ \__\____\_\  \ \__\ \__\ \__\ \__\ \_______\
    \|_______|\___/ /             \|__|/       \|__|\|__|\|__|\_________\|__|\|__|\|__|\|__|\|_______|
             \|___|/                                         \|_________|                             
"""


def run_git_command(command):
    """Runs a Git command and handles errors."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Error: {result.stderr.strip()}")
        return result.stdout.strip()
    except Exception as e:
        print(f"❌ Exception: {e}")
        return ""

def get_unstaged_files():
    """Returns a list of unstaged (modified and untracked) files."""
    output = run_git_command("git ls-files --others --exclude-standard")  # Untracked files
    output2 = run_git_command("git diff --name-only")  # Modified files
    files = output.split("\n") + output2.split("\n")
    return [file.strip() for file in files if file.strip()]

def ensure_git_repo():
    """Ensures the directory is a Git repository, asking the user if needed."""
    if not os.path.exists(".git"):
        choice = input("⚠️  This is not a Git repository! Do you want to initialize one? (y/n): ").strip().lower()
        if choice == "y":
            run_git_command("git init")
            remote_url = input("🌐 Enter remote repository URL (or leave blank to skip): ").strip()
            if remote_url:
                run_git_command(f"git remote add origin {remote_url}")
        else:
            print("🚫 Git repository initialization skipped.")
            exit()

def publish_branch():
    """Checks if an upstream branch is set and publishes if necessary."""
    current_branch = run_git_command("git branch --show-current")
    remote_branch = run_git_command("git rev-parse --abbrev-ref --symbolic-full-name @'{u}'")
    if "fatal" in remote_branch:
        print(f"🚀 Publishing branch '{current_branch}' to remote repository...")
        run_git_command(f"git push --set-upstream origin {current_branch}")

def batch_commit():
    """Handles batch committing and pushing of Git files."""
    print(ASCII_ART)
    print("🚀 Welcome to Vaishal's Git Commit Tool!\n")
    ensure_git_repo()

    files = get_unstaged_files()
    if not files:
        print("✅ No unstaged files found!")
        return

    print(f"\n📂 Total unstaged files: {len(files)}")
    try:
        num = int(input("📌 How many files do you want to stage in each batch? (0 to exit): "))
        if num == 0:
            return
    except ValueError:
        print("❌ Invalid input. Enter a number!")
        return

    while True:
        files = get_unstaged_files()
        if not files:
            print("✅ No unstaged files found!")
            break

        batch = files[:num]
        print(f"\n✅ Staging {len(batch)} files...")
        run_git_command(f"git add {' '.join(batch)}")

        commit_msg = input("📝 Enter commit message: ") or "Batch commit"
        run_git_command(f'git commit -m "{commit_msg}"')

        print("📤 Pushing changes to remote repository...")
        run_git_command("git push")
        publish_branch()

        print("✅ Batch commit and push complete!\n")

    print("🎉 All files committed and pushed successfully!")

if __name__ == "__main__":
    batch_commit()

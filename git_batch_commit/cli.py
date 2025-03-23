import sys

def main():
    print("Git Batch Commit Tool by Vaishal")
    
    if len(sys.argv) > 1:
        print(f"Received arguments: {sys.argv[1:]}")
    else:
        print("No arguments provided. Running in interactive mode.")

if __name__ == "__main__":
    main()

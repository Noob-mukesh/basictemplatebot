import subprocess
import sys

def run_bot_with_live_logs():
    """Run python -m Bot with live console output"""
    try:
        # Start the bot process
        process = subprocess.Popen(
            [sys.executable, "-m", "projects"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Merge stderr with stdout
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        print("Bot process started. Press Ctrl+C to stop.")
        print("-" * 50)
        
        # Read and print output line by line in real-time
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        
        # Check return code
        return_code = process.poll()
        print(f"\nBot process exited with code: {return_code}")
        return return_code
        
    except KeyboardInterrupt:
        print("\nStopping bot process...")
        process.terminate()
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    run_bot_with_live_logs()

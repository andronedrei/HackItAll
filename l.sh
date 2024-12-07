#!/bin/bash

# List of packages and their versions
packages=(
  "cupertino_icons:^1.0.6"
  "provider:^6.1.2"
  "appwrite:^12.0.4"
  "image_picker:^1.1.2"
  "cached_network_image:^3.3.1"
  "flutter_dotenv:^5.1.0"
  "flutter_svg:^2.0.10+1"
  "dart_appwrite:^11.0.3"
  "intl_phone_field:^3.2.0"
  "intl:^0.19.0"
  "video_player:^2.9.1"
  "date_picker_timeline:^1.2.6"
  "flutter_riverpod:^2.5.1"
)

echo "Adding Flutter packages..."

# Loop through each package and add it using flutter pub add
for package in "${packages[@]}"; do
  package_name=$(echo $package | cut -d':' -f1)
  package_version=$(echo $package | cut -d':' -f2)
  echo "Adding $package_name $package_version..."
  flutter pub add "$package_name$package_version"
done

echo "All packages have been added successfully."


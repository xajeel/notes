import json
import numpy as np
import cv2
import os

def load_cameras(camera_path):
    """
    Load camera parameters from JSON file
    """
    with open(camera_path, 'r') as f:
        camera_data = json.load(f)
    return camera_data

def create_camera_path_video(render_dir, camera_path, output_video_path):
    """
    Create a video from rendered images following camera path
    """
    # Load camera data
    camera_data = load_cameras(camera_path)
    
    # Get sorted image list (ensure order matches camera data)
    images = sorted([
        os.path.join(render_dir, cam['img_name']) 
        for cam in camera_data
    ])
    
    # Check if we have enough images
    if not images:
        raise ValueError("No images found in the render directory")
    
    # Read first image to get video parameters
    first_frame = cv2.imread(images[0])
    height, width, _ = first_frame.shape
    
    # Video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (width, height))
    
    # Write video
    for img_path in images:
        frame = cv2.imread(img_path)
        out.write(frame)
    
    out.release()
    
    print(f"Video created at {output_video_path}")

# Example usage
render_dir = 'output/c471b5dc-b/train/ours_30000/renders'
camera_json_path = 'output/c471b5dc-b/cameras.json'
output_video_path = 'output/output_video.mp4'

create_camera_path_video(render_dir, camera_json_path, output_video_path)
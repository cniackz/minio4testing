import os
from PIL import Image
from minio import Minio
from minio.error import S3Error

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "127.0.0.1:9000",
        access_key="minio",
        secret_key="minio123",
        secure=False
    )

    # Get GitHub Env Var
    print(os.environ['GITHUB_WORKSPACE'])
    path_file = os.environ['GITHUB_WORKSPACE'] + "/some-image.jpeg"
    path_file_resized = os.environ['GITHUB_WORKSPACE'] + "/image-resized.jpeg"

    # Download image
    print(client.fget_object("my-bucket", "some-image.jpeg", path_file))

    # Open image
    image = Image.open(path_file)

    # Resize
    new_image = image.resize((500, 500))
    new_image.save(path_file_resized)

    # Next: Upload image to MinIO
    # Next: Verify image was properly uploaded to MinIO

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)

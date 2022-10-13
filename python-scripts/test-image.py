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
    path_file = os.environ['GITHUB_WORKSPACE'] + "/ubuntu-logo.jpeg"
    path_file_resized = os.environ['GITHUB_WORKSPACE'] + "/logo-resized.jpeg"
    logo_verify = os.environ['GITHUB_WORKSPACE'] + "/logo-verify.jpeg"

    # Download image
    print(client.fget_object("my-bucket", "ubuntu-logo.jpeg", path_file))

    # Open image
    image = Image.open(path_file)

    # Resize
    new_image = image.resize((500, 500))
    new_image.save(path_file_resized)

    # Upload image to MinIO
    result = client.fput_object(
        "my-bucket",
        path_file_resized,
        "logo-resized.jpeg"
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
        ),
    )

    # Verify image was properly uploaded to MinIO
    client.fget_object("my-bucket", "logo-resized.jpeg", logo_verify)
    image_one = Image.open(path_file_resized)
    image_two = Image.open(logo_verify)

    diff = ImageChops.difference(image_one, image_two)

    if diff.getbbox():
        print("images are different")
    else:
        print("images are the same")

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)

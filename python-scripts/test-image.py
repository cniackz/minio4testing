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

    # Download image
    print(client.fget_object("my-bucket", "some-image.jpeg", "~/some-image.jpeg"))

    # Open image
    image = Image.open('~/some-image.jpeg')

    # Resize
    new_image = image.resize((500, 500))
    new_image.save('~/image_500.png')

    # Next: Upload image to MinIO
    # Next: Verify image was properly uploaded to MinIO

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)

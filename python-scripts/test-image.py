from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="minio",
        secret_key="minio123",
    )

    # Download image
    print(client.fget_object("my-bucket", "image.png", "~/image.png"))

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)

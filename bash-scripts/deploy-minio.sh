#!/usr/bin/env bash
# Copyright (C) 2022, MinIO, Inc.
#
# This code is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License, version 3,
# along with this program.  If not, see <http://www.gnu.org/licenses/>

echo " "
echo "========================================"
echo "Install mc"
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
mv mc /usr/local/bin/mc

echo " "
echo "========================================"
echo "Install MinIO"
wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
mv minio /usr/local/bin/minio
minio

echo " "
echo "========================================"
echo "Execute MinIO in a process:"
mkdir ~/data1
mkdir ~/data2
mkdir ~/data3
mkdir ~/data4
CI=on MINIO_ROOT_USER=minio MINIO_ROOT_PASSWORD=minio123 minio server ~/data{1...4} --address :9000 --console-address :9001 &
sleep 10
mc alias set myminio http://127.0.0.1:9000 minio minio123

echo " "
echo "========================================"
echo "Place image in a bucket:"
mc mb myminio/my-bucket
touch image.png
echo "a" > image.png
mc cp image.png myminio/my-bucket

echo "Install Python SDK"
echo "========================================"
pip3 install minio

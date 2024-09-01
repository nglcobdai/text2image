# text-to-image

This is a Library to generate images from text.

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **License**     | ![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Environment** | ![Ubuntu](https://img.shields.io/badge/-Ubuntu_22.04_LTS-fad9c1.svg?logo=ubuntu&style=flat) <br> ![Docker](https://img.shields.io/badge/-Docker_v26.0.2-0055a4.svg?logo=docker&style=flat) ![Docker Compose](https://img.shields.io/badge/-Docker_Compose_v2.22.0-0055a4.svg?logo=docker&style=flat) <br>![CUDA](https://img.shields.io/badge/-CUDA_12.1-a4d17c.svg?logo=nvidia&style=flat) ![Python](https://img.shields.io/badge/-Python_3.10-F9DC3E.svg?logo=python&style=flat) ![Poetry](https://img.shields.io/badge/-Poetry-2c2d72.svg?logo=python&style=flat) |
| **Technology**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                 |

## Demo

Example of generated images.

|                                          |                                          |
| ---------------------------------------- | ---------------------------------------- |
| `A cat in a hat`                         | `The photo of Tokyo Tower`               |
| ![Generated Image](./sample/sample1.png) | ![Generated Image](./sample/sample2.png) |

## Requirements

- Docker and docker-compose are required. The versions are as follows.

  - Docker: `v26.0.2`
  - Docker Compose: `v2.22.0`

- Nvidia Driver is required for CUDA `12.1`.

## Getting Started

### 1. Clone Repository

```sh
$ git clone git@github.com:nglcobdai/text-to-image.git
$ cd text-to-image
```

### 2. Create .env file

- copy .env.example to .env

```sh
$ cp .env{.example,}
```

### 3. Docker Build & Run

```sh
$ docker-compose build --no-cache
$ docker-compose run --rm text-to-image
```

### 4. Prepare `order.yml`

- Refer to [order.yml](./config/order.yml) for the format of the file.

| Key        | Description                                                                 |
| ---------- | --------------------------------------------------------------------------- |
| `category` | The category of the image. This is used to determine the image's directory. |
| `tags`     | The tags of the image.                                                      |
| `title`    | The title of the image.                                                     |

### 5. Run Python Script

```sh
$ python text-to-image/main.py
```

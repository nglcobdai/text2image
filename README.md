# text2image

This is a Library to generate images from text.

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **License**     | ![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Environment** | ![Ubuntu](https://img.shields.io/badge/-Ubuntu_22.04_LTS-fad9c1.svg?logo=ubuntu&style=flat) <br> ![Docker](https://img.shields.io/badge/-Docker_v26.0.2-0055a4.svg?logo=docker&style=flat) ![Docker Compose](https://img.shields.io/badge/-Docker_Compose_v2.22.0-0055a4.svg?logo=docker&style=flat) <br>![CUDA](https://img.shields.io/badge/-CUDA_12.5-a4d17c.svg?logo=nvidia&style=flat) ![Python](https://img.shields.io/badge/-Python_3.10-F9DC3E.svg?logo=python&style=flat) ![Poetry](https://img.shields.io/badge/-Poetry-2c2d72.svg?logo=python&style=flat) |
| **Technology**  | ![Hugging Face](https://img.shields.io/badge/huggingface-FFD166?logo=huggingface&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Demo

Example of generated images.

|                                          |                                          |
| :--------------------------------------: | :--------------------------------------: |
|             `A cat in a hat`             |        `The photo of Tokyo Tower`        |
| ![Generated Image](./sample/sample1.png) | ![Generated Image](./sample/sample2.png) |

## Requirements

- Docker and docker-compose are required. The versions are as follows.

  - Docker: `v26.0.2`
  - Docker Compose: `v2.22.0`

- Nvidia Driver is required for CUDA `12.5`.

## Getting Started

### 1. Clone Repository

```sh
$ git clone git@github.com:nglcobdai/text2image.git
$ cd text2image
```

### 2. Create .env file

Copy .env.example to .env

```sh
$ cp .env.example .env.dev
```

Edit .env.dev file

| Key                   | Description                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| DATADRIVE             | The path to the directory where generated image save.                                                                                            |
| HUGGINGFACE_API_TOKEN | The API token for Hugging Face.<br>This token is required to access [the FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) model. |

### 3. Docker Build & Run

```sh
$ docker-compose build --no-cache
$ docker-compose run --rm dev
```

### 4. Run Python Script

```sh
$ python src/__main__.py
```

# selenium-grid
Containerized selenium grid setup. How to setup selenium grid with two nodes (chrome and firefox).

## Pre-requisite
- Python 3 must be installed.
- [Docker for desktop](https://www.docker.com/products/docker-desktop) must be installed
- [chrome webdriver](https://chromedriver.chromium.org/downloads) must be installed.
- [Virtualbox](https://www.virtualbox.org/) must be installed.

## Installation
- Clone git repo and make repo root as current directory.
```bash
git clone https://github.com/qlite-labs/selenium-grid.git
cd selenium-grid
```
- Install dependencies using pip install -r requirements.txt
```bash
pip install -r requirements.txt
```
- create docker-machine with name selenium-grid
```bash
docker-machine create selenium-grid
```
- Setup docker-machine environment using command:
```bash
eval $(docker-machine env selenium-grid)
```
- Get docker-machine ip using command:
```bash
SELENIUM_IP=$(docker-machine ip selenium-grid)
```
- Create docker hub and two nodes (one for chrome and another for firefox) using command:
```bash
docker-compose up -d
```
- Check selenium hub  with two nodes using URL: http://${SELENIUM_IP}:4444/grid/console

## Run test
- Replace SELENIUM_IP in test.py at line number 17.
- Run command `python3 parallel_test_run.py`.
- Refresh selenium hub console. http://${SELENIUM_IP}:4444/grid/console
- It should display running test in parallel.

## Cleanup
- Run following command for cleanup.
```bash
docker-compose down
docker-machine kill selenium-grid
```
.PHONY: test build release

test:
	docker-compose -f docker/dev/docker-compose.yml build

build:
	echo "Hello from build"

release:
	echo "Hello from release"

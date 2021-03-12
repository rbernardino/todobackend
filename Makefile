.PHONY: test build release

test:
	docker-compose -f docker/dev/docker-compose.yml build
	docker-compose -f docker/dev/docker-compose.yml up agent
	docker-compose -f docker/dev/docker-compose.yml up test

build:
	echo "Hello from build"

release:
	echo "Hello from release"
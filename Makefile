REPO ?= structs-py
TAG ?= $(shell git log -1 --format=%h)
IMAGE ?= $(REPO):$(TAG)

build:
	docker build -f Dockerfile -t $(IMAGE) .

test: build
	docker run --rm -v $(PWD):/home/python $(IMAGE) pytest -vv

shell: build
	docker run --rm -v $(PWD):/home/python $(IMAGE) bash

.PHONY: build test shell
REPO ?= structs-py
TAG ?= $(shell git log -1 --format=%h)
IMAGE ?= $(REPO):$(TAG)

build:
	docker build -f Dockerfile -t $(IMAGE) .

test: build
	docker run --rm -v $(PWD):/home/python $(IMAGE) pytest -vv

shell: build
	docker run --rm -v $(PWD):/home/python -it $(IMAGE) bash

pip/clean:
	./setup.py clean \
	&& rm -rf build dist identity_etl_data_types.egg-info

pip/install: pip/clean
	./setup.py bdist && ./setup.py install

.PHONY: build test shell pip/clean pip/install
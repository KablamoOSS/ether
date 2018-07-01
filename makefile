# Makefile for building publishing container
PROJECT = ether
VERSION = $(shell whoami)
REGISTRY = local
APP_IMAGE = $(PROJECT):$(VERSION)
CONTAINER_TAG = latest

imageLocal:
	docker build -t $(APP_IMAGE) .
.PHONY: imageLocal

imageOnly:
	docker build -t $(APP_IMAGE) .
.PHONY: image

image: imageOnly
	docker push $(APP_IMAGE) 
.PHONY: image

publish-image: image
	docker tag $(APP_IMAGE) $(REGISTRY)/ops/$(PROJECT):$(CONTAINER_TAG)
	docker push $(APP_IMAGE)
	docker push $(REGISTRY)/ops/$(PROJECT):$(CONTAINER_TAG)
.PHONY: publish-image


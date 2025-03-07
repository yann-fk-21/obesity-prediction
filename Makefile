build:
	@docker build -t obesity-pred-img .
run:
	@docker run -d --rm -p 8000:8000 obesity-pred-img
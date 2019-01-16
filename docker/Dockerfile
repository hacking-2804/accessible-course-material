FROM alpine

COPY ./ /app/

WORKDIR /app/

RUN cd docker; ./install.sh

EXPOSE 8000

CMD [ "mkdocs", "serve", "-a", "0.0.0.0:8000" ]
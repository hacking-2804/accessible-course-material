FROM alpine

COPY ./ /app/

WORKDIR /app/

RUN cd docker; ./install.sh

EXPOSE 4003

CMD [ "mkdocs", "serve", "-a", "0.0.0.0:4003" ]
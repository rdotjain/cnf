FROM golang:alpine
LABEL maintainer "Rupanshi Jain"

WORKDIR /go/src/app
ADD . .
RUN go mod init
RUN go build -o helloworld

EXPOSE 6112

CMD ["./helloworld"]
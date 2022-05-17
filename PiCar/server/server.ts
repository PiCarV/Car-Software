import { Server } from "socket.io";
import * as http from "http";

const httpServer = http.createServer();
// @ts-ignore
const io = new Server(httpServer, { cors: { origins: ["*"] } });

io.on("connection", (socket: any) => {
  console.log("Client Connected");

  socket.on("drive", (data: any) => {
    io.sockets.emit("drive", data);
  });
  socket.on("steer", (data: any) => {
    io.sockets.emit("steering", data);
  });
  socket.on("pan", (data: any) => {
    io.sockets.emit("pan", data);
  });
  socket.on("tilt", (data: any) => {
    io.sockets.emit("pan", data);
  });
});

io.listen(3000);

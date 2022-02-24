const { Color, Group } = require("./lib/protos/colors_pb.js");
const { GrouperClient } = require("./lib/protos/colors_grpc_web_pb.js");

const grouper = new GrouperClient("http://0.0.0.0:8081");

export function sendColor(color_hex) {
  const request = new Color();
  request.setHex(color_hex);

  grouper.guess(request, {}, (err, res) => {
    if (err) {
      console.error("Error");
      console.error(err);
    }
    console.log(res);
  });
}


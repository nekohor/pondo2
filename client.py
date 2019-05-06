import socket
import json


class SocketClient():

    def __init__(self, ctx):
        self.ctx = ctx

    def get_request(self, ids):
        """return json type"""
        if isinstance(ids, str):
            coil_ids = [ids]
        else:
            coil_ids = ids

        request = {}
        request["requests"] = []
        for coil_id in coil_ids:
            req = {}
            req["coilId"] = coil_id
            req["curDir"] = self.ctx.records.get_cur_dir(coil_id)
            req["factors"] = self.ctx.task.get_factors()
            request["requests"].append(req)

        return json.dumps(request)

    def get_response(self, coil_ids):

        client = socket.socket()
        # 连接到localhost主机的8999端口上去
        client.connect(('localhost', 8999))
        # 把编译成utf-8的数据发送出去
        client.send(self.get_request(coil_ids).encode('utf-8'))
        # 接收数据
        resp = client.recv(10000000)
        coils = json.loads(resp.decode())
        client.close()
        return coils

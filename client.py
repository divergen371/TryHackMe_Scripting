import socket
import time
import sys
import re


def main():
    server_ip = sys.argv[1]
    server_port = 1337
    old_num = 0

    while server_port != 9765:
        try:
            if server_port == 1337:
                print(
                    f"Connecting to {server_ip} waiting for port {server_port} to become available."
                )

            s = socket.socket()
            s.connect((server_ip, server_port))

            get_req = f"GET / HTTP/1.0\r\nHost: {server_ip}:{server_port}\r\n\r\n"
            s.send(get_req.encode("utf-8"))

            while True:
                response = s.recv(1024)
                if len(response) < 1:
                    break

                data = response.decode("utf-8")

            op, new_num, next_port = assign_data(data)
            old_num = do_math(op, old_num, new_num)
            print(f"Current number is {old_num}, moving onto Port {next_port}")

            server_port = next_port

            s.close()

        except:
            s.close()
            time.sleep(3)
            pass

    print(f"The final answer is {round(old_num,2)}")


def do_math(op, old_num, new_num):
    """

    :param op: str
    :param old_num: int
    :param new_num: int
    :return: int, None
    """
    if op == "add":
        return old_num + new_num
    elif op == "minus":
        return old_num - new_num
    elif op == "divide":
        return old_num / new_num
    elif op == "multiply":
        return old_num * new_num
    else:
        return None


def assign_data(data: str):
    """

    :param data: str
    :return: str, int
    """
    data_arr = re.split(" |\*|\n", data)
    data_arr = list(filter(None, data_arr))
    op = data_arr[-3]
    new_num = float(data_arr[-2])
    next_port = int(data_arr[-1])
    return op, new_num, next_port


if __name__ == "__main__":
    main()

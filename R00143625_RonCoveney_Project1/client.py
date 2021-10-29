import logging

import grpc
import word_game_pb2
import word_game_pb2_grpc


class Client:
    # Class client to run for grpc client, only functionality we need from class is the run function

    def run(self):
        # this method will run the client to listen on port 50051 of localhost

        with grpc.insecure_channel('localhost:50051') as channel:
            current_score = 0

            # grpc stub to call methods defined by services
            stub = word_game_pb2_grpc.WordGameStub(channel)
            print("Spelling Bee!")

            # calling the ping rpc to get the pangram by server, no need to pass anything as we need data from
            # server only
            response = stub.ping(word_game_pb2.Empty())
            print(response.pangram)

            # infinite loop for letting client make multiple requests to server
            while True:
                try:
                    word = input("Enter word > ")
                    # calling the getWord rpc to get the score and message from the server about the word
                    # passing the word got from input as a parameter to the rpc getWord
                    response = stub.getWord(word_game_pb2.Word(word=word))

                    # fetching values from the response from server and printing them accordingly
                    print(response.pangram)
                    current_score += response.score
                    print("{} Current score: {}".format(
                        response.msg, current_score))

                except KeyboardInterrupt:
                    # keyboardInterrupt exception for Ctrl+c command on the cmd.
                    # closing channel by callback to unsubscribe method of channel before exiting python script
                    print("KeyboardInterrupt")
                    channel.unsubscribe(self.close)
                    exit()

    def close(self, channel):
        # method to close the channel/client
        channel.close()


if __name__ == '__main__':
    logging.basicConfig()
    client = Client()
    client.run()

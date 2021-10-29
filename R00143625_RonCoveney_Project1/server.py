from concurrent import futures
import logging
import grpc
import word_game_pb2
import word_game_pb2_grpc
from dictionary_lookup import DictionaryLookup


class Servicer(word_game_pb2_grpc.WordGameServicer):
    # Servicer class to add functionalities to the grpc server

    def __init__(self):
        # initialize the Servicer object, create DictionaryLookup object as the instance variable
        super().__init__()

        self.pangram = DictionaryLookup()
        self.pangram.set_pangram()

    def getWord(self, request, context):
        # method to respond the rpc getWord

        # getting the msg and score for the word requested by the client.
        msg, score = self.pangram.check_word(request.word)

        pangram = self.pangram.get_pangram()
        # sending response to client
        return word_game_pb2.Score(msg=msg, score=score, pangram=pangram)

    def ping(self, request, context):
        # method to respond the rpc ping
        pangram = self.pangram.get_pangram()
        # sending response to client
        return word_game_pb2.Pangram(pangram=pangram)


class Server:
    # Server class to run a grpc server

    def serve(self):
        # method to create and run server on port 50051 of localhost
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        word_game_pb2_grpc.add_WordGameServicer_to_server(Servicer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        print("Server is running")

        try:
            server.wait_for_termination()
            pass
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    server = Server()
    server.serve()

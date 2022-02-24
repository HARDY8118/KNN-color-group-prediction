/**
 * @fileoverview gRPC-Web generated client stub for colors
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.colors = require('./colors_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.colors.GrouperClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.colors.GrouperPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.colors.Color,
 *   !proto.colors.Group>}
 */
const methodDescriptor_Grouper_Guess = new grpc.web.MethodDescriptor(
  '/colors.Grouper/Guess',
  grpc.web.MethodType.UNARY,
  proto.colors.Color,
  proto.colors.Group,
  /**
   * @param {!proto.colors.Color} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.colors.Group.deserializeBinary
);


/**
 * @param {!proto.colors.Color} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.colors.Group)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.colors.Group>|undefined}
 *     The XHR Node Readable Stream
 */
proto.colors.GrouperClient.prototype.guess =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/colors.Grouper/Guess',
      request,
      metadata || {},
      methodDescriptor_Grouper_Guess,
      callback);
};


/**
 * @param {!proto.colors.Color} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.colors.Group>}
 *     Promise that resolves to the response
 */
proto.colors.GrouperPromiseClient.prototype.guess =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/colors.Grouper/Guess',
      request,
      metadata || {},
      methodDescriptor_Grouper_Guess);
};


module.exports = proto.colors;


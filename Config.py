#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
class BilstmCrfConfig(object):
    # data
    train_data = "./data/train"
    test_data = "./data/test"
    vocab_path = "./Vocab/vocab.txt"
    embedding_path = "./Embedding/glove200.txt"
    trimed_path = "./Embedding/embedding_trim.npy"
    logdir = 'logdir'
    #Traing
    EPOCH = 100
    maxlen = 250
    batch_size = 32
    num_class = 12
    dropout_rate = 0.5
    lr = 0.0001
    min_vocab = 1
    num_layer = 2
    num_units = 200
    sinusoid = True
    use_pretrain = True
    exponential_decay = False
    cell='lstm'
    use_crf = True
    regulation = True # use batch normalize
    normalize=True # 
    #model
    #attention if use concat position_dim can not equal embed_dim
    #otherwise they must equal!
    position_dim = 200
    embed_dim = 200
    embeddig_mode = "concat"#"concat" or "add"
    

















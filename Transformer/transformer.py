import torch as th
import torch.nn.functional as F

from torch import nn

class EncoderRNN(nn.Module):
    '''
    将输入序列编码为隐藏状态向量
    '''
    def __init__(self, input_size, hidden_size, dropout_p=0.1):
        super(EncoderRNN, self).__init__()
        self.hidden_size = hidden_size
        self.embedding = nn.Embedding(input_size, hidden_size) # 将输入序列中的每个元素映射成对应的稠密向量
        self.rnn = nn.RNN(hidden_size, hidden_size, batch_first=True)
        self.dropout = nn.Dropout(dropout_p)
        
    def forward(self, x):
        x = self.embedding(x) # 嵌入操作
        x = self.dropout(x) # 随机失活
        output, hidden = self.rnn(x) # 编码
        
        return output, hidden


def main():
    encoder = EncoderRNN(input_size=10, hidden_size=5)
    input_vector = th.tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
    output, hidden = encoder(input_vector)
    
    print("输入向量的维度：", input_vector.size())
    print("输出向量的维度：", output.size())
    print("最终隐藏状态的维度：", hidden.size())

if __name__ == '__main__':
    main()
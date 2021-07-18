import torch
import torch.nn as nn

# class to implement self attention
class SelfAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(SelfAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads

        assert (self.head_dim * heads == embed_size), "Embed size needs to be div by heads"

        # defining the linear layers we'll use
        self.values = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.keys = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.queries = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.fc_output = nn.Linear(heads*self.head_dim, embed_size)  # concatenation of multi-heads

    def forward(self, values, keys, query, mask):
        N = query.shape[0] # how many samples sent at same time
        value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]

        # Split embbending into self.heads pieces. Before it was (N, value_len, embed_size) == (num_sentences, num_words, embed_size)
        values = values.reshape(N, value_len, self.heads, self.head_dim)
        keys = values.reshape(N, key_len, self.heads, self.head_dim)
        queries = query.reshape(N, query_len, self.heads, self.head_dim)

        # we want to multiply the queries with the keys
        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys]) # matrix multiplication when several dims
        # queries shape: (N, query_len, heads, head_dim)
        # keys shape: (N, key_len, heads, head_dim)
        # energy shape: (N, heads, query_len, key_len) # query_len is the target source sentence and key_len is the source sentence

        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))  # Where mask == 0 we put -inf to the energy

        # Attention formula
        attention = torch.softmax(energy / (self.embed_size ** (1/2)), dim=3)

        out = torch.einsum("nhql,nlhd->nqhd", [attention, values])
        # attention shape: (N, heads, query_len, key_len)
        # values shapes: (N, value_len, heads, heads_dim)
        # (N, query_len, heads, head_dim)

        out = out.reshape(N, query_len, self.heads*self.head_dim)  # Concatenation (flatten last 2 dim)

        out = self.fc_output(out) # Send it through the fc_out, there's no change of dim

        return out

class TransformerBlock(nn.Module):
    def __init__(self, embed_size, heads, dropout, forward_expansion):
        super(TransformerBlock, self).__init__()
        self.attention = SelfAttention(embed_size, heads)
        self.norm1 = nn.LayerNorm(e)  # Like BatchNorm, but here is the average for each exemple and not for the batch
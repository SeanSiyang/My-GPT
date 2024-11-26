from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline

model_path = "E:/Codes/models/gp2-chinese-poem"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)
text_generator = TextGenerationPipeline(model, tokenizer)

result = text_generator("[CLS]我 爱 张 迪 ，", max_length=100, do_sample=True)

print(result)

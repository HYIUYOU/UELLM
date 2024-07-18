import argparse
import torch
from model import MODE


def parse_args():
    parser = argparse.ArgumentParser()
    # Model
    parser.add_argument("--device", type=str, default="0", help="")
    parser.add_argument("--mode", type=str, default="glm3", help="")
    parser.add_argument("--model_path", type=str, default="output_dir/", help="")
    parser.add_argument("--max_length", type=int, default=2048, help="")
    parser.add_argument("--do_sample", type=bool, default=True, help="")
    parser.add_argument("--top_p", type=float, default=0.8, help="")
    parser.add_argument("--temperature", type=float, default=0.8, help="")
    return parser.parse_args()


def predict_one_sample(instruction, input, model, tokenizer, args):
    result, _ = model.chat(tokenizer, instruction + input, max_length=args.max_length, do_sample=args.do_sample,
                           top_p=args.top_p, temperature=args.temperature)
    return result


if __name__ == '__main__':
    args = parse_args()
    model = MODE[args.mode]["model"].from_pretrained(args.model_path, device_map="cuda:{}".format(args.device),
                                                     torch_dtype=torch.float16)
    tokenizer = MODE[args.mode]["tokenizer"].from_pretrained(args.model_path)
    import json

    # Read JSON file
    with open('file.json', 'r') as f:
        data = json.load(f)
        
    instruction = "You are now an information extraction model. Please help me extract the related triples with the relation contents of \"performance failure\", \"component failure\", \"composition\" and \"detection tool\". The triples are connected by \"_\" and separated by \n. Text:"
    input = "Fault phenomenon: The engine water temperature is high, the fan always rotates at low speed, and the high speed gear does not work, especially when the air conditioner is turned on."
    r = predict_one_sample(instruction, input, model, tokenizer, args)
    print(r)




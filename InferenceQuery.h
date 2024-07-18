#ifndef INFERENCEQUERY_H
#define INFERENCEQUERY_H

#include <string>

// Defining the InferenceQuery structure
struct InferenceQuery
{
    string label;
    std::string SLO;
    std::string language;
    std::string type;
    std::string prompt;

    // :param label: Inference_Query identifier, the same identifier indicates contextual connection
    // :param SLO: Inference_Query SLO
    // :param language: Inference_Query language (for simplicity, each Inference query is set to be one of Chinese C and English E)
    // :param type: Inference_Query type (for simplicity, each Inference query is set to be computer vision CV, audio AD, video VD, natural language NLP, sentiment analysis EMO)
    // :param prompt: Inference_Query prompt
    // :param model: Inference_Query specified model type (the default value is null, indicating that the required model is not specified)

    //    InferenceQuery(std::string label, std::string SLO, std::string language, std::string type, std::string prompt)
    //            : label(label), SLO(SLO), language(language), type(type), prompt(prompt) {}

    // size_t operator()(const InferenceQuery& query) const {
    //     // You can choose any attribute that is suitable as an input to a hash function.
    //     // Here we use the label string to calculate the hash value
    //     return std::hash<std::string>{}(query.label);
    // }
};

#endif // INFERENCEQUERY_H

////inference query class
// class InferenceQuery {
// public:
//     InferenceQuery(string label, string SLO, string language,  string type,  string prompt,  string model = "null")
//             : label(label), SLO(SLO), language(language), type(type), prompt(prompt), model(model) {}
//
//     // :param label: Inference_Query label
//     // :param SLO: Inference_Query SLO
//     // :param language: Inference_Query language (for simplicity, assume that each Inference query is one of Chinese C and English E)
//     // :param type: Inference_Query type (for simplicity, assume that each Inference query is computer vision CV, audio AD, video VD, natural language NLP, sentiment analysis EMO)
//     // :param prompt: Inference_Query prompt
//     // :param model: Inference_Query specified model type (the default value is null, indicating that the required model is not specified)
//
//     // Getter methods for class members
//     string getLabel() const { return label; }
//     string getSLO() const { return SLO; }
//     string getLanguage() const { return language; }
//     string getType() const { return type; }
//     string getPrompt() const { return prompt; }
//     string getModel() const { return model; }
//
//
// private:
//     string label;
//     string SLO;
//     string language;
//     string type;
//     string prompt;
//     string model;
// };

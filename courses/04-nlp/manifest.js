/* Маніфест курсу: порядок блоків і тем, назви. Єдине джерело для обгортки
   сторінок (courses/assets/course.js). Згенеровано з index.html. */
window.COURSE = {
 "id": "04-nlp",
 "title": "Обробка природної мови",
 "blocks": [
  {
   "n": 1,
   "title": "Текст як дані",
   "topics": [
    {
     "slug": "01-text-is-hard",
     "num": "01",
     "title": "Чому текст складніший за таблицю"
    },
    {
     "slug": "02-tokenization",
     "num": "02",
     "title": "Токенізація: як текст стає числами"
    },
    {
     "slug": "03-morphology",
     "num": "03",
     "title": "Морфологія: лематизація і стемінг"
    },
    {
     "slug": "04-bag-of-words",
     "num": "04",
     "title": "Мішок слів"
    },
    {
     "slug": "05-tfidf",
     "num": "05",
     "title": "TF-IDF"
    }
   ]
  },
  {
   "n": 2,
   "title": "Класичний NLP",
   "topics": [
    {
     "slug": "06-text-classification",
     "num": "06",
     "title": "Класифікація текстів"
    },
    {
     "slug": "07-metrics",
     "num": "07",
     "title": "Метрики й оцінка"
    },
    {
     "slug": "08-topic-modeling",
     "num": "08",
     "title": "Тематичне моделювання"
    },
    {
     "slug": "09-search",
     "num": "09",
     "title": "Пошук і схожість"
    },
    {
     "slug": "10-rules-regex",
     "num": "10",
     "title": "Правила й регулярні вирази"
    }
   ]
  },
  {
   "n": 3,
   "title": "Векторні представлення",
   "topics": [
    {
     "slug": "11-distributional-semantics",
     "num": "11",
     "title": "Дистрибутивна семантика"
    },
    {
     "slug": "12-word2vec",
     "num": "12",
     "title": "Word2Vec"
    },
    {
     "slug": "13-glove-fasttext",
     "num": "13",
     "title": "GloVe і FastText"
    },
    {
     "slug": "14-vector-arithmetic",
     "num": "14",
     "title": "Арифметика векторів"
    },
    {
     "slug": "15-embedding-bias",
     "num": "15",
     "title": "Оцінка й упередженість ембедингів"
    }
   ]
  },
  {
   "n": 4,
   "title": "Послідовні моделі",
   "topics": [
    {
     "slug": "16-language-model",
     "num": "16",
     "title": "Мовна модель: наступне слово"
    },
    {
     "slug": "17-rnn",
     "num": "17",
     "title": "RNN для тексту"
    },
    {
     "slug": "18-lstm-gru",
     "num": "18",
     "title": "LSTM і GRU"
    },
    {
     "slug": "19-seq2seq",
     "num": "19",
     "title": "seq2seq і машинний переклад"
    },
    {
     "slug": "20-rnn-limits",
     "num": "20",
     "title": "Межі RNN"
    }
   ]
  },
  {
   "n": 5,
   "title": "Трансформер",
   "topics": [
    {
     "slug": "21-transformer-architecture",
     "num": "21",
     "title": "Архітектура і чому витіснила RNN"
    },
    {
     "slug": "22-self-attention",
     "num": "22",
     "title": "Self-attention покроково"
    },
    {
     "slug": "23-multihead-masking",
     "num": "23",
     "title": "Multi-head, позиційне кодування, маскування"
    },
    {
     "slug": "24-transformer-training",
     "num": "24",
     "title": "Навчання трансформера"
    }
   ]
  },
  {
   "n": 6,
   "title": "Передтреновані моделі",
   "topics": [
    {
     "slug": "25-pretraining",
     "num": "25",
     "title": "Ідея передтренування"
    },
    {
     "slug": "26-bert",
     "num": "26",
     "title": "BERT"
    },
    {
     "slug": "27-bert-in-practice",
     "num": "27",
     "title": "BERT у роботі"
    },
    {
     "slug": "28-gpt-family",
     "num": "28",
     "title": "GPT-родина"
    },
    {
     "slug": "29-t5-bart",
     "num": "29",
     "title": "T5 і BART"
    },
    {
     "slug": "30-multilingual",
     "num": "30",
     "title": "Багатомовність і українська"
    }
   ]
  },
  {
   "n": 7,
   "title": "Прикладні задачі",
   "topics": [
    {
     "slug": "31-text-generation",
     "num": "31",
     "title": "Як модель породжує текст"
    },
    {
     "slug": "32-ner",
     "num": "32",
     "title": "NER"
    },
    {
     "slug": "33-question-answering",
     "num": "33",
     "title": "Question answering"
    },
    {
     "slug": "34-summarization",
     "num": "34",
     "title": "Сумаризація"
    },
    {
     "slug": "35-sentiment-in-production",
     "num": "35",
     "title": "Аналіз тональності в бою"
    },
    {
     "slug": "36-rag",
     "num": "36",
     "title": "RAG і векторні бази"
    }
   ]
  },
  {
   "n": 8,
   "title": "Дорога до LLM",
   "topics": [
    {
     "slug": "37-scaling",
     "num": "37",
     "title": "Що змінює масштаб"
    },
    {
     "slug": "38-instruction-tuning-rlhf",
     "num": "38",
     "title": "Instruction tuning і RLHF"
    },
    {
     "slug": "39-peft-lora",
     "num": "39",
     "title": "PEFT і LoRA"
    },
    {
     "slug": "40-limits",
     "num": "40",
     "title": "Межі мовних моделей"
    }
   ]
  }
 ]
};

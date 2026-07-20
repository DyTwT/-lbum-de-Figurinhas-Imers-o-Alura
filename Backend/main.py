from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

app = FastAPI()

# Configuração do CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista de figurinhas do álbum feminista
# Todas as 19 figurinhas estão disponíveis na pasta figurinhas/
figurinhas = [
    {"id": 1,  "nome": "Mary Wollstonecraft",   "categoria": "Pioneiras do Feminismo",      "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2,  "nome": "Olympe de Gouges",       "categoria": "Pioneiras do Feminismo",      "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3,  "nome": "Sojourner Truth",        "categoria": "Feminismo e Raça",            "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4,  "nome": "Susan B. Anthony",       "categoria": "Sufragistas",                 "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5,  "nome": "Elizabeth Cady Stanton", "categoria": "Sufragistas",                 "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6,  "nome": "Simone de Beauvoir",     "categoria": "Feminismo Filosófico",        "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7,  "nome": "Virginia Woolf",         "categoria": "Feminismo e Literatura",      "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8,  "nome": "Bell Hooks",             "categoria": "Feminismo Interseccional",    "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9,  "nome": "Angela Davis",           "categoria": "Feminismo e Raça",            "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Judith Butler",          "categoria": "Teoria Queer e Gênero",       "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Bertha Lutz",            "categoria": "Feminismo Brasileiro",        "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Nísia Floresta",         "categoria": "Feminismo Brasileiro",        "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Djamila Ribeiro",        "categoria": "Feminismo Brasileiro",        "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Marielle Franco",        "categoria": "Feminismo Brasileiro",        "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Heleieth Saffioti",      "categoria": "Feminismo Brasileiro",        "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Malala Yousafzai",       "categoria": "Ativismo Global",             "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Emma Watson",            "categoria": "Ativismo Global",             "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Chimamanda Ngozi Adichie","categoria": "Feminismo e Literatura",     "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Greta Thunberg",         "categoria": "Ativismo Global",             "imagem_url": "/figurinhas/19/imagem"},
]


@app.get("/figurinhas")
def listar_figurinhas():
    """Retorna a lista completa de figurinhas do álbum."""
    return figurinhas


@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    """
    Retorna a imagem de uma figurinha pelo seu ID.
    Usa glob para encontrar o arquivo com prefixo '{id:02d}' na pasta figurinhas/.
    """
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)

    if not arquivos:
        raise HTTPException(status_code=404, detail=f"Imagem da figurinha {id} não encontrada.")

    return FileResponse(arquivos[0])

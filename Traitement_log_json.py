{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "8c28f9fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from urllib.request import Request, urlopen\n",
    "import os\n",
    "import json\n",
    "\n",
    "\n",
    "#renvoie l'url du fichier JSON à partir de 'url'\n",
    "#urlReplay: l'url du replay\n",
    "def getUrlJson(urlReplay) -> str: \n",
    "    req = Request(urlReplay, headers={'User-Agent': 'Mozilla/5.0'})\n",
    "    file = urlopen(req).read()\n",
    "    idxEndJson = file.find(b\".json\")+5\n",
    "    idxStartJson = file.find(b\"https:\", idxEndJson -100, idxEndJson)\n",
    "    urlJson = file[idxStartJson: idxEndJson].decode(\"utf-8\") \n",
    "    return urlJson\n",
    "\n",
    "#ouvre et nettoie un fichier json et renvoie le contenu\n",
    "#ulrJson : l'url du fichier JSON\n",
    "def clearJson(urlJson):\n",
    "    req = Request(urlJson, headers={'User-Agent': 'Mozilla/5.0'})\n",
    "    file = urlopen(req).read()\n",
    "    json_ = json.loads(file)\n",
    "    json_ = json_['log'].split('\\n')\n",
    "    return json_\n",
    "    \n",
    "#sauve le 'content' dans un fichier JSON. Si le dossier de sauvegarde n'existe pas, il est créé\n",
    "#path: le chemin du dossier dans lequel sauver le fichier\n",
    "#name: le nom du fichier JSON\n",
    "#content: le contenu à sauver\n",
    "def saveJson(path, nameFile, content):\n",
    "    if not os.path.exists(path):\n",
    "        os.makedirs(path)\n",
    "    fullName = path + '/' + nameFile\n",
    "    with open(fullName, 'w') as outfile:\n",
    "        json.dump(content, outfile)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "db4dd13f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#test avec une URL\n",
    "def testUrl(urlReplay = 'https://replay.pokemonshowdown.com/gen8oublitz-1408634835') :\n",
    "    url = getUrlJson(urlReplay)\n",
    "    print(url)\n",
    "    contentJson = clearJson(url)\n",
    "    print(\"Content imported and cleared\")\n",
    "    nameFile = (url.split('/')[-1])\n",
    "    saveJson('JSON_logs', nameFile, contentJson)\n",
    "    print(f\"File {'JSON_logs/'+nameFile} saved\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "8e00968f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://replay.pokemonshowdown.com/gen8oublitz-1408634835.json\n",
      "Content imported and cleared\n",
      "File JSON_logs/gen8oublitz-1408634835.json JSON saved\n"
     ]
    }
   ],
   "source": [
    "testUrl()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9bb66213",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

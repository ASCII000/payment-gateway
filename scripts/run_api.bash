# Import utils
source scripts/utils.bash

# Get all folders
folders=$(find . -maxdepth 1 -type d)

# Possible python commands
possible_python_commands=("python3" "python" "py")

# Environment folders
env_folders=("env" "venv")

# Loop for check main python command
cm_python=""
for command in "${possible_python_commands[@]}"; do
    if command -v "$command" &>/dev/null; then
        "$command" --version &>/dev/null
        if [ $? -eq 0 ]; then
            cm_python=$command
            break
        fi
    fi
done

if [ -z "$cm_python" ]; then
    echo "Nenhum comando Python encontrado. Abortando."
    exit 1
fi

for env_folder in "${env_folders[@]}"; do
    if [ -d "$env_folder" ]; then
        echo "🌱 Virtualenv '$env_folder' já existe. Ativando..."
    else
        echo "🌱 Criando virtualenv '$env_folder'..."
        try $cm_python -m venv "$env_folder"
    fi

    source "$env_folder/Scripts/activate" || echo "🔴 Falha ao ativar venv."
    echo "🟢 Ambiente virtual ativado com sucesso."
    break
done

# Detect site-packages path multiplataforma
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    site_packages_path="$env_folder/Lib/site-packages"
else
    python_version=$($cm_python -c 'import sys; print("python{}.{}".format(sys.version_info[0], sys.version_info[1]))')
    site_packages_path="$env_folder/lib/$python_version/site-packages"
fi

# Conta pacotes instalados
count=$(find "$site_packages_path" -mindepth 1 -type d | wc -l)

echo "📦 Pacotes encontrados: $count"

# Checa se pacotes estão instalados de fato
if ! $cm_python -c "import fastapi" &>/dev/null; then
    echo "📦 Instalando dependências com poetry..."
    poetry install
fi

# Run the api
try $cm_python src/main.py

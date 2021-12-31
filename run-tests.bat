@echo off
mypy --strict frostbyte
pylint frostbyte
python -m readme_renderer README.rst -o README-PROOF.html
pytest test --cov=./frostbyte
coverage html
@pause

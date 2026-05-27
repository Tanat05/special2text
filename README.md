# special2text

`special2text`는 장식된 특수문자, 풀가로 문자, 다양한 스크립트 및 수학적 서체 문자를 일반 텍스트(ASCII/한글 등)로 변환하는 작은 Python 유틸리티입니다.

설치

```bash
pip install special2text
```

로컬에서 설치하려면:

```bash
pip install .
```

사용법

파이썬에서:

```python
from special2text import special_en, special_ko, special_text

print(special_en('Ｈｅｌｌｏ！ １２３'))        # Hello! 123
print(special_ko('안૮ત્રુ하⋌⫣요̆̈', cleanup_non_korean=True))
```

명령행 도구(설치 시 제공):

```bash
special2text
# 또는
python -m special2text.special2text
```

기여 및 라이선스

프로젝트는 MIT 라이선스입니다. 개선/이슈는 PR을 통해 환영합니다.

# -*- coding: utf-8 -*-
"""Connect Mode 전용: 한 `### Connect Mode` 블록을 3개 Suite raw로 분할.

Connect Mode는 Notion에서 `📍 Edit Role: Editor 이상` 아래 최상위 불릿 3개로 나뉜다:
  - Canvas & Stage (131개)   → CanvasStage (suite 1364)
  - Left Panel (173개)       → LeftPanel  (suite 1362)
  - Right Panel (81개)       → RightPanel (suite 1363)
각 그룹 불릿의 하위(토글들)를 한 탭 내려(de-indent) 그룹별 raw.md로 재루팅하고,
이미지 폴더를 그룹별로 복사한다. 이후 convert_api/upload를 그룹 키로 실행하면 됨.

선행: python migrate/extract_menu.py ConnectMode <dump>  (build/ConnectMode_raw.md + _images 생성)
사용: python migrate/split_connectmode.py
"""
import os, re, shutil, io, sys

GROUPS = [('CanvasStage', 'Canvas & Stage'),
          ('LeftPanel', 'Left Panel'),
          ('RightPanel', 'Right Panel')]
ROLE = '📍 **Edit Role: Editor 이상**'


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    src = os.path.join('build', 'ConnectMode_raw.md')
    lines = open(src, encoding='utf-8').read().split('\n')

    # 최상위(d=0) 그룹 불릿 위치 찾기
    pos = {}
    for key, name in GROUPS:
        for i, l in enumerate(lines):
            if l.startswith('- ') and name in l:
                pos[key] = i
                break
        if key not in pos:
            sys.exit(f'그룹 불릿을 못 찾음: {name}')
    ordered = sorted(((pos[k], k) for k in pos))

    for n, (start, key) in enumerate(ordered):
        end = ordered[n + 1][0] if n + 1 < len(ordered) else len(lines)
        content = lines[start + 1:end]
        # 한 탭 de-indent (그룹 하위는 d>=1 → 토글이 top-level d=0 이 됨)
        deind = [(l[1:] if l.startswith('\t') else l) for l in content]
        text = ROLE + '\n' + '\n'.join(deind).rstrip() + '\n'
        out = os.path.join('build', f'{key}_raw.md')
        open(out, 'w', encoding='utf-8').write(text)
        # 이미지 폴더 복사(공용 풀 — convert가 uuid로 필요한 것만 사용)
        dst_img = os.path.join('build', f'{key}_images')
        if os.path.isdir(dst_img):
            shutil.rmtree(dst_img)
        shutil.copytree(os.path.join('build', 'ConnectMode_images'), dst_img)
        print(f'{key}: {len(deind)} lines → {out}  (images copied)')
        print(f'   다음: python migrate/convert_api.py {key} && python migrate/upload.py {key}')


if __name__ == '__main__':
    main()

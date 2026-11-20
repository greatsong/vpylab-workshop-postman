친구 = group()
몸 = box(group=친구, size=vec(1.6, 1, 0.6),
        color=color.cyan)
왼눈 = sphere(group=친구, pos=vec(-0.36, 0.15, 0.32),
            radius=0.15)
오른눈 = sphere(group=친구, pos=vec(0.36, 0.15, 0.32),
             radius=0.15)
등 = sphere(group=친구, pos=vec(0, 0.67, 0),
           radius=0.23, color=color.orange)

def 이동(e):
    if e.key == "right":
        친구.pos.x += 0.3
    if e.key == "left":
        친구.pos.x -= 0.3
scene.bind("keydown", 이동)

def 인사(e):
    # 고리몽이 만든 등불 동작
    등.emissive = not 등.emissive
    # 도란몽이 인사 소리를 넣을 자리
    play_note("G4", 0.3)
scene.bind("click", 인사)

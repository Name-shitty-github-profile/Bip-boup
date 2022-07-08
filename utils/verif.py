from .role import add_role
role_dispo: dict = {
  "python": 995007159517577297,
  "py": 995007159517577297,
  "javascript": 995042222384893983,
  "js": 995042222384893983,
  "étudiant/e": 995007160645861417
}
async def verif(member, bot):
  msg = await member.send("Bienvenue !\nTu va devoir coder un petit peu pour rejoindre ce serveur ^^\nLanguage : pinguin language\nVoici la syntaxe ^^\n```\nfn add_me(role_name)\nfn add_me(role2_name)\n```\n**Language disponibles**\n```\nPython\nJavascript\n```")
  code = await bot.wait_for("message", check=lambda m : m.author.id == member.id and msg.channel.id == m.channel.id)
  e, role = pinguin_process(code.content, member.id)
  await member.send(f"```console\n{e}```\nVoici vos roles ajoutés\n```" + ", ".join(role) + "\n```")
  for i in role: add_role(member.id, role_dispo[i.lower()])

def pinguin_process(content: str, user_id):
  lines: list = content.split('\n')
  roles: list = []
  for i in range(len(lines)):
    line = lines[i]
    i += 1
    if not line.endswith(')'):
      return f"Line does not stop\nSource(Line {i}) : {line}\nVeuillez ressayer avec `?role`\nVous allez quand même être vérifé(e)", ["Étudiant/e"]
    if line.startswith("fn "):
      line = line[3:]
      if line.startswith("add_me("):
        line = line[7:-1]
        if line.lower() not in role_dispo:
          return f"Unknown Function\nSource(Line {i}) : {line}\nVeuillez ressayer avec `?role`\nVous allez quand même être vérifé(e)", ["Étudiant/e"]
        roles.append(line)
      else:
        return f"Unknown Function\nSource(Line {i}) : {line}\nVeuillez ressayer avec `?role`\nVous allez quand même être vérifé(e)", ["Étudiant/e"]
    else:
      return f"Unknown type\nSource(Line {i}) : {line}\nVeuillez ressayer avec `?role`\nVous allez quand même être vérifé(e)", ["Étudiant/e"]
  roles.append('Étudiant/e')
  return f'Code exited with no error !', roles

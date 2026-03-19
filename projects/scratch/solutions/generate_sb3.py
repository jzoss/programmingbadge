#!/usr/bin/env python3
"""
⚜️ A SCOUT IS TRUSTWORTHY ⚜️
==============================
This is the COMPLETED SOLUTION for the Grade Calculator.
A Scout is trustworthy — don't peek at this until you've tried
solving the challenges on your own first!

The first point of the Scout Law reminds us to be honest and
do our best work. Give it a real try before looking here!
==============================

Generate a Scratch 3.0 (.sb3) Grade Calculator — SOLUTION project.
Programming Merit Badge — Requirement 5c

All TODO challenges have been completed:
  ✅ Challenge #3: Tracks highest and lowest scores
  ✅ Challenge (bonus): Pass/fail message after grade output

Run:  python3 generate_sb3.py
Output: grade_calculator.sb3
"""

import json
import zipfile
import hashlib
import sys

# =====================================================================
# ASSET DATA
# =====================================================================

BACKDROP_SVG = (
    '<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<rect width="480" height="360" fill="#f0f4ff"/>'
    '</svg>'
)

SPRITE_SVG = (
    '<svg version="1.1" width="80" height="100" viewBox="0 0 80 100" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<circle cx="40" cy="40" r="35" fill="#4C97FF" stroke="#3373CC" stroke-width="3"/>'
    '<circle cx="30" cy="32" r="5" fill="white"/>'
    '<circle cx="50" cy="32" r="5" fill="white"/>'
    '<circle cx="31" cy="33" r="2.5" fill="#333"/>'
    '<circle cx="51" cy="33" r="2.5" fill="#333"/>'
    '<path d="M 28 52 Q 40 62 52 52" stroke="#333" stroke-width="2.5" '
    'fill="none" stroke-linecap="round"/>'
    '</svg>'
)


def md5hex(data):
    return hashlib.md5(data.encode("utf-8")).hexdigest()


# =====================================================================
# BLOCK BUILDER HELPERS
# =====================================================================

_id_counter = 0
blocks = {}
comments = {}

VARS = {
    "numberOfTests": "v_nt",
    "totalScore": "v_ts",
    "counter": "v_ct",
    "average": "v_av",
    "grade": "v_gr",
    "message": "v_mg",
    # SOLUTION: Challenge #3 — highest/lowest tracking
    "highestScore": "v_hi",
    "lowestScore": "v_lo",
}


def uid():
    global _id_counter
    _id_counter += 1
    return f"blk{_id_counter}"


def str_lit(val):
    return [1, [10, str(val)]]

def num_lit(val):
    return [1, [4, str(val)]]

def var_num(name):
    return [3, [12, name, VARS[name]], [4, ""]]

def var_str(name):
    return [3, [12, name, VARS[name]], [10, ""]]

def blk_num(bid, default=""):
    return [3, bid, [4, str(default)]]

def blk_str(bid, default=""):
    return [3, bid, [10, str(default)]]

def cond(bid):
    return [2, bid]

def stk(bid):
    return [2, bid]


def mkblk(bid, opcode, *, inputs=None, fields=None,
          parent=None, nxt=None, shadow=False, top=False, x=0, y=0):
    b = {
        "opcode": opcode,
        "next": nxt,
        "parent": parent,
        "inputs": inputs or {},
        "fields": fields or {},
        "shadow": shadow,
        "topLevel": top,
    }
    if top:
        b["x"] = x
        b["y"] = y
    blocks[bid] = b


def add_comment(block_id, text, x=0, y=0, w=220, h=150):
    cid = f"cmt{len(comments)}"
    comments[cid] = {
        "blockId": block_id,
        "x": x, "y": y,
        "width": w, "height": h,
        "minimized": True,
        "text": text,
    }


# =====================================================================
# PRE-ASSIGN BLOCK IDs
# =====================================================================

B_FLAG = uid(); B_WELCOME = uid(); B_ASK_COUNT = uid()
B_SET_NT = uid(); B_SET_TS0 = uid(); B_SET_CT0 = uid()
B_SET_HI0 = uid(); B_SET_LO0 = uid()
B_REPEAT = uid(); B_SET_AVG = uid(); B_IF_A = uid()
B_SAY_AVG = uid(); B_SAY_GR = uid(); B_SAY_MSG = uid()
B_SAY_HI = uid(); B_SAY_LO = uid(); B_IF_PASS = uid()
B_SAY_PASS = uid(); B_SAY_FAIL = uid()
B_SAY_BYE = uid()

B_ASK_SCORE = uid(); B_CHG_TS = uid(); B_CHG_CT = uid()
B_IF_NEW_HI = uid(); B_GT_HI = uid()
B_IF_NEW_LO = uid(); B_LT_LO = uid()

B_SET_GR_A = uid(); B_SET_MG_A = uid()
B_IF_B = uid(); B_SET_GR_B = uid(); B_SET_MG_B = uid()
B_IF_C = uid(); B_SET_GR_C = uid(); B_SET_MG_C = uid()
B_IF_D = uid(); B_SET_GR_D = uid(); B_SET_MG_D = uid()
B_SET_GR_F = uid(); B_SET_MG_F = uid()

B_ANS1 = uid(); B_JOIN_Q = uid(); B_ADD_CT1 = uid(); B_ANS2 = uid()
B_DIV = uid()
B_NOT_A = uid(); B_LT_A = uid()
B_NOT_B = uid(); B_LT_B = uid()
B_NOT_C = uid(); B_LT_C = uid()
B_NOT_D = uid(); B_LT_D = uid()
B_JOIN_AVG = uid(); B_ROUND = uid(); B_JOIN_GR = uid()
B_JOIN_HI = uid(); B_JOIN_LO = uid()
B_NOT_PASS = uid(); B_LT_PASS = uid()
B_ANS_HI = uid(); B_ANS_LO = uid()
B_ANS_SET_HI = uid(); B_SET_HI_VAR = uid()
B_ANS_SET_LO = uid(); B_SET_LO_VAR = uid()

# =====================================================================
# BUILD BLOCKS
# =====================================================================

mkblk(B_FLAG, "event_whenflagclicked", top=True, x=50, y=50, nxt=B_WELCOME)

mkblk(B_WELCOME, "looks_sayforsecs",
      inputs={"MESSAGE": str_lit("Welcome to the Grade Calculator! 📊"), "SECS": num_lit(2)},
      parent=B_FLAG, nxt=B_ASK_COUNT)

mkblk(B_ASK_COUNT, "sensing_askandwait",
      inputs={"QUESTION": str_lit("How many test scores do you have?")},
      parent=B_WELCOME, nxt=B_SET_NT)

mkblk(B_ANS1, "sensing_answer", parent=B_SET_NT)
mkblk(B_SET_NT, "data_setvariableto",
      inputs={"VALUE": blk_str(B_ANS1)},
      fields={"VARIABLE": ["numberOfTests", VARS["numberOfTests"]]},
      parent=B_ASK_COUNT, nxt=B_SET_TS0)

mkblk(B_SET_TS0, "data_setvariableto",
      inputs={"VALUE": str_lit("0")},
      fields={"VARIABLE": ["totalScore", VARS["totalScore"]]},
      parent=B_SET_NT, nxt=B_SET_CT0)

mkblk(B_SET_CT0, "data_setvariableto",
      inputs={"VALUE": str_lit("0")},
      fields={"VARIABLE": ["counter", VARS["counter"]]},
      parent=B_SET_TS0, nxt=B_SET_HI0)

# SOLUTION: Initialize highest to 0, lowest to 100
mkblk(B_SET_HI0, "data_setvariableto",
      inputs={"VALUE": str_lit("0")},
      fields={"VARIABLE": ["highestScore", VARS["highestScore"]]},
      parent=B_SET_CT0, nxt=B_SET_LO0)

mkblk(B_SET_LO0, "data_setvariableto",
      inputs={"VALUE": str_lit("100")},
      fields={"VARIABLE": ["lowestScore", VARS["lowestScore"]]},
      parent=B_SET_HI0, nxt=B_REPEAT)

# ---- REPEAT LOOP ----

mkblk(B_REPEAT, "control_repeat",
      inputs={"TIMES": var_num("numberOfTests"), "SUBSTACK": stk(B_ASK_SCORE)},
      parent=B_SET_LO0, nxt=B_SET_AVG)

mkblk(B_ADD_CT1, "operator_add",
      inputs={"NUM1": var_num("counter"), "NUM2": num_lit(1)},
      parent=B_JOIN_Q)
mkblk(B_JOIN_Q, "operator_join",
      inputs={"STRING1": str_lit("Enter score #"), "STRING2": blk_str(B_ADD_CT1)},
      parent=B_ASK_SCORE)

mkblk(B_ASK_SCORE, "sensing_askandwait",
      inputs={"QUESTION": blk_str(B_JOIN_Q, "Enter score:")},
      parent=B_REPEAT, nxt=B_CHG_TS)

mkblk(B_ANS2, "sensing_answer", parent=B_CHG_TS)
mkblk(B_CHG_TS, "data_changevariableby",
      inputs={"VALUE": blk_num(B_ANS2)},
      fields={"VARIABLE": ["totalScore", VARS["totalScore"]]},
      parent=B_ASK_SCORE, nxt=B_CHG_CT)

mkblk(B_CHG_CT, "data_changevariableby",
      inputs={"VALUE": num_lit(1)},
      fields={"VARIABLE": ["counter", VARS["counter"]]},
      parent=B_CHG_TS, nxt=B_IF_NEW_HI)

# SOLUTION: if answer > highestScore then set highestScore to answer
mkblk(B_ANS_HI, "sensing_answer", parent=B_GT_HI)
mkblk(B_GT_HI, "operator_gt",
      inputs={"OPERAND1": [3, B_ANS_HI, [10, ""]], "OPERAND2": var_str("highestScore")},
      parent=B_IF_NEW_HI)

mkblk(B_ANS_SET_HI, "sensing_answer", parent=B_SET_HI_VAR)
mkblk(B_SET_HI_VAR, "data_setvariableto",
      inputs={"VALUE": [3, B_ANS_SET_HI, [10, ""]]},
      fields={"VARIABLE": ["highestScore", VARS["highestScore"]]},
      parent=B_IF_NEW_HI)

mkblk(B_IF_NEW_HI, "control_if",
      inputs={"CONDITION": cond(B_GT_HI), "SUBSTACK": stk(B_SET_HI_VAR)},
      parent=B_CHG_CT, nxt=B_IF_NEW_LO)

# SOLUTION: if answer < lowestScore then set lowestScore to answer
mkblk(B_ANS_LO, "sensing_answer", parent=B_LT_LO)
mkblk(B_LT_LO, "operator_lt",
      inputs={"OPERAND1": [3, B_ANS_LO, [10, ""]], "OPERAND2": var_str("lowestScore")},
      parent=B_IF_NEW_LO)

mkblk(B_ANS_SET_LO, "sensing_answer", parent=B_SET_LO_VAR)
mkblk(B_SET_LO_VAR, "data_setvariableto",
      inputs={"VALUE": [3, B_ANS_SET_LO, [10, ""]]},
      fields={"VARIABLE": ["lowestScore", VARS["lowestScore"]]},
      parent=B_IF_NEW_LO)

mkblk(B_IF_NEW_LO, "control_if",
      inputs={"CONDITION": cond(B_LT_LO), "SUBSTACK": stk(B_SET_LO_VAR)},
      parent=B_IF_NEW_HI)

# ---- COMPUTE AVERAGE ----

mkblk(B_DIV, "operator_divide",
      inputs={"NUM1": var_num("totalScore"), "NUM2": var_num("numberOfTests")},
      parent=B_SET_AVG)
mkblk(B_SET_AVG, "data_setvariableto",
      inputs={"VALUE": blk_num(B_DIV)},
      fields={"VARIABLE": ["average", VARS["average"]]},
      parent=B_REPEAT, nxt=B_IF_A)

# ---- GRADE IF/ELSE CHAIN ----

mkblk(B_LT_A, "operator_lt",
      inputs={"OPERAND1": var_str("average"), "OPERAND2": str_lit("90")}, parent=B_NOT_A)
mkblk(B_NOT_A, "operator_not", inputs={"OPERAND": cond(B_LT_A)}, parent=B_IF_A)
mkblk(B_SET_GR_A, "data_setvariableto",
      inputs={"VALUE": str_lit("A")}, fields={"VARIABLE": ["grade", VARS["grade"]]},
      parent=B_IF_A, nxt=B_SET_MG_A)
mkblk(B_SET_MG_A, "data_setvariableto",
      inputs={"VALUE": str_lit("Amazing work! 🌟")}, fields={"VARIABLE": ["message", VARS["message"]]},
      parent=B_SET_GR_A)
mkblk(B_IF_A, "control_if_else",
      inputs={"CONDITION": cond(B_NOT_A), "SUBSTACK": stk(B_SET_GR_A), "SUBSTACK2": stk(B_IF_B)},
      parent=B_SET_AVG, nxt=B_SAY_AVG)

mkblk(B_LT_B, "operator_lt",
      inputs={"OPERAND1": var_str("average"), "OPERAND2": str_lit("80")}, parent=B_NOT_B)
mkblk(B_NOT_B, "operator_not", inputs={"OPERAND": cond(B_LT_B)}, parent=B_IF_B)
mkblk(B_SET_GR_B, "data_setvariableto",
      inputs={"VALUE": str_lit("B")}, fields={"VARIABLE": ["grade", VARS["grade"]]},
      parent=B_IF_B, nxt=B_SET_MG_B)
mkblk(B_SET_MG_B, "data_setvariableto",
      inputs={"VALUE": str_lit("Great job! Keep it up! 💪")}, fields={"VARIABLE": ["message", VARS["message"]]},
      parent=B_SET_GR_B)
mkblk(B_IF_B, "control_if_else",
      inputs={"CONDITION": cond(B_NOT_B), "SUBSTACK": stk(B_SET_GR_B), "SUBSTACK2": stk(B_IF_C)},
      parent=B_IF_A)

mkblk(B_LT_C, "operator_lt",
      inputs={"OPERAND1": var_str("average"), "OPERAND2": str_lit("70")}, parent=B_NOT_C)
mkblk(B_NOT_C, "operator_not", inputs={"OPERAND": cond(B_LT_C)}, parent=B_IF_C)
mkblk(B_SET_GR_C, "data_setvariableto",
      inputs={"VALUE": str_lit("C")}, fields={"VARIABLE": ["grade", VARS["grade"]]},
      parent=B_IF_C, nxt=B_SET_MG_C)
mkblk(B_SET_MG_C, "data_setvariableto",
      inputs={"VALUE": str_lit("Not bad! Study a bit more! 📚")}, fields={"VARIABLE": ["message", VARS["message"]]},
      parent=B_SET_GR_C)
mkblk(B_IF_C, "control_if_else",
      inputs={"CONDITION": cond(B_NOT_C), "SUBSTACK": stk(B_SET_GR_C), "SUBSTACK2": stk(B_IF_D)},
      parent=B_IF_B)

mkblk(B_LT_D, "operator_lt",
      inputs={"OPERAND1": var_str("average"), "OPERAND2": str_lit("60")}, parent=B_NOT_D)
mkblk(B_NOT_D, "operator_not", inputs={"OPERAND": cond(B_LT_D)}, parent=B_IF_D)
mkblk(B_SET_GR_D, "data_setvariableto",
      inputs={"VALUE": str_lit("D")}, fields={"VARIABLE": ["grade", VARS["grade"]]},
      parent=B_IF_D, nxt=B_SET_MG_D)
mkblk(B_SET_MG_D, "data_setvariableto",
      inputs={"VALUE": str_lit("You passed! Let's improve! 💡")}, fields={"VARIABLE": ["message", VARS["message"]]},
      parent=B_SET_GR_D)

mkblk(B_SET_GR_F, "data_setvariableto",
      inputs={"VALUE": str_lit("F")}, fields={"VARIABLE": ["grade", VARS["grade"]]},
      parent=B_IF_D, nxt=B_SET_MG_F)
mkblk(B_SET_MG_F, "data_setvariableto",
      inputs={"VALUE": str_lit("Don't give up! Ask for help! 🤝")}, fields={"VARIABLE": ["message", VARS["message"]]},
      parent=B_SET_GR_F)
mkblk(B_IF_D, "control_if_else",
      inputs={"CONDITION": cond(B_NOT_D), "SUBSTACK": stk(B_SET_GR_D), "SUBSTACK2": stk(B_SET_GR_F)},
      parent=B_IF_C)

# ---- OUTPUT ----

mkblk(B_ROUND, "operator_round", inputs={"NUM": var_num("average")}, parent=B_JOIN_AVG)
mkblk(B_JOIN_AVG, "operator_join",
      inputs={"STRING1": str_lit("Your average is: "), "STRING2": blk_str(B_ROUND)},
      parent=B_SAY_AVG)
mkblk(B_SAY_AVG, "looks_sayforsecs",
      inputs={"MESSAGE": blk_str(B_JOIN_AVG), "SECS": num_lit(3)},
      parent=B_IF_A, nxt=B_SAY_GR)

mkblk(B_JOIN_GR, "operator_join",
      inputs={"STRING1": str_lit("Your letter grade: "), "STRING2": var_str("grade")},
      parent=B_SAY_GR)
mkblk(B_SAY_GR, "looks_sayforsecs",
      inputs={"MESSAGE": blk_str(B_JOIN_GR), "SECS": num_lit(3)},
      parent=B_SAY_AVG, nxt=B_SAY_MSG)

mkblk(B_SAY_MSG, "looks_sayforsecs",
      inputs={"MESSAGE": var_str("message"), "SECS": num_lit(3)},
      parent=B_SAY_GR, nxt=B_SAY_HI)

# SOLUTION: Show highest score
mkblk(B_JOIN_HI, "operator_join",
      inputs={"STRING1": str_lit("Highest score: "), "STRING2": var_str("highestScore")},
      parent=B_SAY_HI)
mkblk(B_SAY_HI, "looks_sayforsecs",
      inputs={"MESSAGE": blk_str(B_JOIN_HI), "SECS": num_lit(2)},
      parent=B_SAY_MSG, nxt=B_SAY_LO)

# SOLUTION: Show lowest score
mkblk(B_JOIN_LO, "operator_join",
      inputs={"STRING1": str_lit("Lowest score: "), "STRING2": var_str("lowestScore")},
      parent=B_SAY_LO)
mkblk(B_SAY_LO, "looks_sayforsecs",
      inputs={"MESSAGE": blk_str(B_JOIN_LO), "SECS": num_lit(2)},
      parent=B_SAY_HI, nxt=B_IF_PASS)

# SOLUTION: Pass/fail — average >= 60 = pass
mkblk(B_LT_PASS, "operator_lt",
      inputs={"OPERAND1": var_str("average"), "OPERAND2": str_lit("60")},
      parent=B_NOT_PASS)
mkblk(B_NOT_PASS, "operator_not",
      inputs={"OPERAND": cond(B_LT_PASS)},
      parent=B_IF_PASS)

mkblk(B_SAY_PASS, "looks_sayforsecs",
      inputs={"MESSAGE": str_lit("You PASSED! Great work!"), "SECS": num_lit(3)},
      parent=B_IF_PASS)
mkblk(B_SAY_FAIL, "looks_sayforsecs",
      inputs={"MESSAGE": str_lit("You need to retake this class. Don't give up!"), "SECS": num_lit(3)},
      parent=B_IF_PASS)

mkblk(B_IF_PASS, "control_if_else",
      inputs={"CONDITION": cond(B_NOT_PASS), "SUBSTACK": stk(B_SAY_PASS), "SUBSTACK2": stk(B_SAY_FAIL)},
      parent=B_SAY_LO, nxt=B_SAY_BYE)

mkblk(B_SAY_BYE, "looks_sayforsecs",
      inputs={"MESSAGE": str_lit("Thanks for using the Grade Calculator! 🎓"), "SECS": num_lit(2)},
      parent=B_IF_PASS)

# ---- SOLUTION COMMENTS ----

add_comment(B_IF_NEW_HI,
            "SOLUTION — Challenge #3: Tracks highest\n"
            "and lowest scores. Compares each answer\n"
            "to current high/low and updates if needed.",
            x=480, y=-50, w=250, h=120)

add_comment(B_IF_PASS,
            "SOLUTION — Pass/fail message:\n"
            "If average < 60, shows a retake message.\n"
            "Otherwise shows a passed message.",
            x=480, y=150, w=250, h=120)

# =====================================================================
# BUILD & WRITE
# =====================================================================

backdrop_md5 = md5hex(BACKDROP_SVG)
sprite_md5 = md5hex(SPRITE_SVG)

project = {
    "targets": [
        {
            "isStage": True, "name": "Stage",
            "variables": {}, "lists": {}, "broadcasts": {},
            "blocks": {}, "comments": {},
            "currentCostume": 0,
            "costumes": [{"assetId": backdrop_md5, "name": "backdrop1",
                          "md5ext": f"{backdrop_md5}.svg", "dataFormat": "svg",
                          "rotationCenterX": 240, "rotationCenterY": 180}],
            "sounds": [], "volume": 100, "layerOrder": 0,
            "tempo": 60, "videoTransparency": 50, "videoState": "on",
            "textToSpeechLanguage": None,
        },
        {
            "isStage": False, "name": "Grade Calculator — SOLUTION",
            "variables": {vid: [vname, 0] for vname, vid in VARS.items()},
            "lists": {}, "broadcasts": {},
            "blocks": blocks, "comments": comments,
            "currentCostume": 0,
            "costumes": [{"assetId": sprite_md5, "name": "calculator",
                          "md5ext": f"{sprite_md5}.svg", "dataFormat": "svg",
                          "rotationCenterX": 40, "rotationCenterY": 50}],
            "sounds": [], "volume": 100, "layerOrder": 1,
            "visible": True, "x": 0, "y": 0, "size": 100,
            "direction": 90, "draggable": False, "rotationStyle": "all around",
        },
    ],
    "monitors": [], "extensions": [],
    "meta": {"semver": "3.0.0", "vm": "0.2.0", "agent": ""},
}

output_path = sys.argv[1] if len(sys.argv) > 1 else "grade_calculator.sb3"

with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("project.json", json.dumps(project, ensure_ascii=False))
    zf.writestr(f"{backdrop_md5}.svg", BACKDROP_SVG)
    zf.writestr(f"{sprite_md5}.svg", SPRITE_SVG)

print(f"Created: {output_path} (SOLUTION)")
print(f"  {len(blocks)} blocks, {len(comments)} comments, {len(VARS)} variables")

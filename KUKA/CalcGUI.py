import tkinter as tk
from tkinter import ttk
import math
import json
import os

# --------------------------------------------------------
# GENEROWANIE PUNKTÓW I DEKLARACJI
# --------------------------------------------------------

def generate_declarations(Xc, Yc, Zc, D, N, A_const, B_max, C_max):
    R = D / 2.0
    decl_output = ""
    points = []

    for i in range(N):
        theta = 2 * math.pi * i / N

        X = Xc + R * math.cos(theta)
        Y = Yc + R * math.sin(theta)
        Z = Zc

        B = -B_max * math.cos(theta)
        C = C_max * math.sin(theta)

        wireFeed = 4.000
        robotVelocity = 0.25 / 60

        Pname = f"P{i+1}"
        points.append(Pname)

        decl = (f"DECL E6POS XP{i + 1}={{X {X:.3f}, Y {Y:.3f}, Z {Z:.3f}, "
                f"A {A_const:.3f}, B {B:.4f}, C {C:.4f}, S 2, T 10}}\n"
                f"DECL FDAT FP{i + 1}={{TOOL_NO 6,BASE_NO 20,IPO_FRAME #BASE,POINT2[] \" \"}}\n"
                f"DECL LDAT LCPDAT{i + 1}={{VEL 0.200000,ACC 100.000,APO_DIST 500.000,APO_FAC 50.0000,AXIS_VEL 100.000,"
                f"AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 100.000,EXAX_IGN 0}}\n"
                f"DECL stArcDat_T WP{i + 1}={{WdatId[] \"WP{i + 1}\",Info {{Version 303030366}}}}\n")

        strike = (
            f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] "f"\"WDAT{i + 1}\""",Strike {JobModeId[] \"GMAW synergic S2-Step\","
            "ParamSetId[] "f"\"Set1\""f",StartTime 0.500000,PreFlowTime 1.00000,Channel1 3449.00,Channel2 {wireFeed},Channel3 0.0,"
            "Channel4 0.0,Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0,PurgeTime 0.0},"
            "Weld {JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] "f"\"Set2\""","
            f"Velocity {robotVelocity},Channel1 3449.00,Channel2 {wireFeed},Channel3 0.0,Channel4 0.0,Channel5 0.0,"
            "Channel6 0.0,Channel7 0.0,Channel8 0.0},Weave {Pattern #None,Length 4.00000,Amplitude 2.00000,"
            "Angle 0.0,LeftSideDelay 0.0,RightSideDelay 0.0}}\n")

        weld = (
            f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] "f"\"WDAT{i + 1}\""",Weld {JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] "
            ""f"\"Set2\""f",Velocity {robotVelocity},Channel1 3449.00,Channel2 {wireFeed},Channel3 0.0,Channel4 0.0,Channel5 0.0,"
            "Channel6 0.0,Channel7 0.0,Channel8 0.0},Weave {Pattern #None,Length 4.00000,Amplitude 2.00000,Angle 0.0,"
            "LeftSideDelay 0.0,RightSideDelay 0.0}}\n")

        crater = (
            f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] "f"\"WDAT{i + 1}\""",Crater {JobModeId[] \"GMAW synergic S2-Step\","
            "ParamSetId[] "f"\"Set1\""f",CraterTime 0.500000,PostflowTime 1.00000,Channel1 3449.00,Channel2 {wireFeed},"
            "Channel3 0.0,Channel4 0.0,Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0,BurnBackTime 0.0}}\n")

        if i == 0:
            decl += (strike)
        elif i == N - 1:
            decl += (crater)
        else:
            decl += (weld)

        decl_output += decl + "\n"

    return decl_output, points


# --------------------------------------------------------
# SZABLONY PROGRAMU
# --------------------------------------------------------

template_ARCON = """
;FOLD ARCON WDAT{I} LIN {P} Vel=0.2 m/s CPDAT{I} Tool[6]:Fajka45 Base[20]:PP_noga ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arconlin; Kuka.IsGlobalPoint=False; 
;Kuka.PointName={P}; Kuka.BlendingEnabled=False; Kuka.MoveDataName=CPDAT{I};
;Kuka.VelocityPath=0.2; Kuka.CurrentCDSetIndex=0; Kuka.MovementParameterFieldEnabled=True;
;ArcTech.WdatVarName=WDAT{I}; ArcTech.Basic=3.3.3.366
;ENDFOLD
$BWDSTART = FALSE
LDAT_ACT = LCPDAT{I}
FDAT_ACT = F{P}
BAS(#CP_PARAMS, 0.2)
SET_CD_PARAMS (0)
TRIGGER WHEN DISTANCE = 1 DELAY = ArcGetDelay(#PreDefinition, WDAT{I}) DO ArcMainNG(#PreDefinition, WDAT{I}, W{P}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOn, WDAT{I}) DELAY = ArcGetDelay(#GasPreflow, WDAT{I}) DO ArcMainNG(#GasPreflow, WDAT{I}, W{P}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOn, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOnMoveStd, WDAT{I}, W{P}) PRIO = -1 
ArcMainNG(#ArcOnBeforeMoveStd, WDAT{I}, W{P})
LIN X{P}
ArcMainNG(#ArcOnAfterMoveStd, WDAT{I}, W{P})
;ENDFOLD
"""

template_ARCSWI = """
;FOLD ARCSWI WDAT{I} CIRC {Phelp} {P} CPDAT{I} Tool[6]:Fajka45 Base[20]:PP_noga ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arcswicirc; Kuka.IsGlobalPoint=False;
;Kuka.PointName={P}; Kuka.HelpPointName={Phelp}; Kuka.BlendingEnabled=True;
;Kuka.MoveDataName=CPDAT{I}; Kuka.VelocityPath=0.2; Kuka.CurrentCDSetIndex=0;
;Kuka.MovementParameterFieldEnabled=True; ArcTech.WdatVarName=WDAT{I};
;ArcTech.Basic=3.3.3.366
;ENDFOLD
$BWDSTART = FALSE
LDAT_ACT = LCPDAT{I}
FDAT_ACT = F{P}
BAS(#CP_PARAMS, gArcBasVelDefinition)
SET_CD_PARAMS (0)
TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO ArcMainNG(#ArcSwiMoveStd, WDAT{I}, W{P}, W{Phelp}) PRIO = -1
ArcMainNG(#ArcSwiBeforeMoveStd, WDAT{I}, W{P}, W{Phelp})
CIRC X{Phelp}, X{P} C_Dis C_Dis
ArcMainNG(#ArcSwiAfterMoveStd, WDAT{I}, W{P}, W{Phelp})
;ENDFOLD
"""

template_ARCOFF = """
;FOLD ARCOFF WDAT{I} CIRC {Phelp} {P} CPDAT{I} Tool[6]:Fajka45 Base[20]:PP_noga ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arcoffcirc; Kuka.IsGlobalPoint=False;
;Kuka.PointName={P}; Kuka.HelpPointName={Phelp}; Kuka.BlendingEnabled=False;
;Kuka.MoveDataName=CPDAT{I}; Kuka.VelocityPath=0.2; Kuka.CurrentCDSetIndex=0;
;Kuka.MovementParameterFieldEnabled=True; ArcTech.WdatVarName=WDAT{I}; 
;ArcTech.Basic=3.3.3.366
;ENDFOLD
$BWDSTART = FALSE
LDAT_ACT = LCPDAT{I}
FDAT_ACT = F{P}
BAS(#CP_PARAMS, gArcBasVelDefinition)
SET_CD_PARAMS (0)
TRIGGER WHEN PATH = ArcGetPath(#ArcOffBefore, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOffBeforeOffStd, WDAT{I}, W{P}, W{Phelp}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOff, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOffMoveStd, WDAT{I}, W{P}, W{Phelp}) PRIO = -1 
ArcMainNG(#ArcOffBeforeMoveStd, WDAT{I}, W{P}, W{Phelp})
CIRC X{Phelp}, X{P}
ArcMainNG(#ArcOffAfterMoveStd, WDAT{I}, W{P}, W{Phelp})
;ENDFOLD
"""

def generate_program(points):
    out = ""
    # ARCON
    out += template_ARCON.format(P=points[0], I=1)

    # ARCSWI (co drugi punkt)
    for i in range(2, len(points)-1, 2):
        out += template_ARCSWI.format(P=points[i], Phelp=points[i-1], I=i+1)

    # ARCOFF
    out += template_ARCOFF.format(P=points[-1], Phelp=points[-2], I=len(points))

    return out

SETTINGS_FILE = "settings.json"

def save_settings():
    data = {
        "Xc": entry_Xc.get(),
        "Yc": entry_Yc.get(),
        "Zc": entry_Zc.get(),
        "D": entry_D.get(),
        "N": entry_N.get(),
        "A_const": entry_A.get(),
        "B_max": entry_B.get(),
        "C_max": entry_C.get()
    }
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f)


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return

    with open(SETTINGS_FILE, "r") as f:
        data = json.load(f)

    entry_Xc.delete(0, tk.END)
    entry_Xc.insert(0, data.get("Xc", ""))

    entry_Yc.delete(0, tk.END)
    entry_Yc.insert(0, data.get("Yc", ""))

    entry_Zc.delete(0, tk.END)
    entry_Zc.insert(0, data.get("Zc", ""))

    entry_D.delete(0, tk.END)
    entry_D.insert(0, data.get("D", ""))

    entry_N.delete(0, tk.END)
    entry_N.insert(0, data.get("N", ""))

    entry_A.delete(0, tk.END)
    entry_A.insert(0, data.get("A_const", ""))

    entry_B.delete(0, tk.END)
    entry_B.insert(0, data.get("B_max", ""))

    entry_C.delete(0, tk.END)
    entry_C.insert(0, data.get("C_max", ""))



# --------------------------------------------------------
# FUNKCJA WYWOŁYWANA PO KLIKNIĘCIU PRZYCISKU
# --------------------------------------------------------

def on_generate():
    Xc = float(entry_Xc.get())
    Yc = float(entry_Yc.get())
    Zc = float(entry_Zc.get())
    D = float(entry_D.get())
    N = int(entry_N.get())
    A_const = float(entry_A.get())
    B_max = float(entry_B.get())
    C_max = float(entry_C.get())

    declarations, points = generate_declarations(Xc, Yc, Zc, D, N, A_const, B_max, C_max)
    program = generate_program(points)

    text_decl.delete("1.0", tk.END)
    text_decl.insert(tk.END, declarations)

    text_prog.delete("1.0", tk.END)
    text_prog.insert(tk.END, program)


# --------------------------------------------------------
# GUI TKINTER
# --------------------------------------------------------


root = tk.Tk()
root.title("Generator KUKA ARC — GUI")

# ----- FRAME KONFIGURACJI (grid) -----
frame_cfg = ttk.Frame(root, padding=10)
frame_cfg.grid(row=0, column=0, sticky="nw")

labels = ["Xc", "Yc", "Zc", "Średnica D", "Liczba punktów N", "A_const", "B_max", "C_max"]
defaults = ["123", "100.5", "-97", "20", "13", "-90", "25", "25"]
entries = []

for i, (lbl, val) in enumerate(zip(labels, defaults)):
    ttk.Label(frame_cfg, text=lbl).grid(row=i, column=0, sticky="w")
    e = ttk.Entry(frame_cfg)
    e.insert(0, val)
    e.grid(row=i, column=1)
    entries.append(e)

entry_Xc, entry_Yc, entry_Zc, entry_D, entry_N, entry_A, entry_B, entry_C = entries
load_settings()

ttk.Button(frame_cfg, text="GENERUJ", command=on_generate).grid(row=8, column=0, columnspan=2, pady=10)

# ----- FRAME WYNIKÓW (pack) -----
frame_out = ttk.Frame(root)
frame_out.grid(row=0, column=1, sticky="ne")

text_decl = tk.Text(frame_out, width=220, height=25)
text_decl.pack(side="top", padx=10, pady=5)

text_prog = tk.Text(frame_out, width=220, height=25)
text_prog.pack(side="bottom", padx=10, pady=5)


def on_closing():
    save_settings()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()


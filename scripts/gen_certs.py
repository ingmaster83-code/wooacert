# -*- coding: utf-8 -*-
"""증명서 발급 안내 콘텐츠 -> 정적 HTML 페이지 생성"""
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent.parent
CERT_DIR = ROOT / "cert"
BASE_URL = "https://wooacert.wooahouse.com"

CATEGORIES = [
    ("family", "가족·신분", "#1D4ED8", "가족관계증명서, 주민등록등본 등 신원을 증명하는 서류"),
    ("tax", "세금·소득", "#D97706", "소득·납세 사실을 증명하는 서류"),
    ("insurance", "4대보험", "#0F766E", "건강보험·국민연금·고용보험 가입 이력 서류"),
    ("military", "병역·범죄", "#7C3AED", "병역사항, 범죄경력을 증명하는 서류"),
    ("edu", "학력", "#DB2777", "졸업·재학 사실을 증명하는 서류"),
    ("estate", "부동산", "#059669", "부동산 권리관계를 증명하는 서류"),
    ("travel", "여행", "#2563EB", "해외 출국에 필요한 서류"),
]
CAT_MAP = {c[0]: c for c in CATEGORIES}

CERTS = [
    dict(
        slug="family-relation-cert", cat="family", emoji="👨‍👩‍👧",
        name="가족관계증명서",
        title="가족관계증명서 인터넷발급 방법·수수료 안내",
        desc="가족관계증명서를 정부24·전자가족관계등록시스템에서 온라인 발급받는 방법, 수수료(무료), 필요서류, 일반/상세 증명서 차이를 한 번에 정리했습니다.",
        keywords="가족관계증명서 발급, 가족관계증명서 인터넷발급, 가족관계증명서 정부24, 가족관계증명서 무료발급, 가족관계증명서 상세",
        issuing_org="법원행정처(대법원)",
        online=True,
        online_desc="정부24(gov.kr) 또는 대법원 전자가족관계등록시스템(efamily.scourt.go.kr)에서 공동인증서·간편인증(카카오·PASS 등)으로 로그인 후 즉시 무료 발급·출력할 수 있습니다.",
        offline_desc="가까운 시·구·읍·면·동 주민센터(전국 어디서나 가능)를 방문해 신분증을 제시하면 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)", "공동인증서 또는 간편인증(온라인 시)"],
        validity="발급일로부터 통상 3개월 이내 제출을 요구하는 기관이 많음(제출처마다 다름)",
        intro="가족관계증명서는 본인을 기준으로 부모·배우자·자녀 등 가족관계를 증명하는 서류로, 2008년 호주제 폐지 이후 기존 호적등본을 대신하고 있습니다. 상속·보험금 청구·자녀 학교 제출·주택청약 등 본인과 가족관계를 확인해야 하는 거의 모든 행정·금융 절차에서 요구됩니다.",
        notice="'일반증명서'와 '상세증명서' 두 종류가 있습니다. 일반증명서는 현재 혼인 중인 배우자·생존한 자녀만 표시되고, 상세증명서는 이혼한 배우자·사망한 가족까지 모두 표시됩니다. 제출 기관이 요구하는 종류를 미리 확인 후 발급하세요.",
        uses=["상속 절차", "보험금 청구", "자녀 학교 제출", "주택청약", "혼인신고 확인", "연말정산 부양가족 증빙"],
        tips=[
            "온라인 발급 시 '일반' 또는 '상세' 중 제출처가 요구하는 종류를 정확히 선택하세요 — 잘못 발급하면 다시 발급해야 합니다.",
            "주민센터 무인민원발급기에서도 발급 가능하며, 지문 인증만 되면 신분증 없이도 발급됩니다.",
            "미성년 자녀의 증명서는 부모(법정대리인)가 온라인으로 발급받을 수 있습니다.",
        ],
        faqs=[
            ("가족관계증명서와 기본증명서의 차이는 무엇인가요?",
             "가족관계증명서는 부모·배우자·자녀 등 '가족 구성원'을 보여주고, 기본증명서는 본인의 출생·개명·국적 등 '본인 신상 정보'만 보여줍니다. 서로 다른 용도라 제출처가 요구하는 서류를 정확히 확인해야 합니다."),
            ("외국에서도 발급받을 수 있나요?",
             "재외공관(대사관·영사관)을 방문하면 발급 신청이 가능하며, 국내 가족이 대신 온라인으로 발급해 우편·이메일로 보내주는 방법도 있습니다."),
            ("타인이 대신 발급받을 수 있나요?",
             "온라인 발급은 본인 인증이 필요해 대리 발급이 불가능합니다. 방문 발급은 위임장과 위임자·대리인 신분증을 지참하면 가능합니다."),
        ],
    ),
    dict(
        slug="basic-cert", cat="family", emoji="🪪",
        name="기본증명서",
        title="기본증명서 인터넷발급 방법·수수료 안내",
        desc="기본증명서를 정부24에서 무료로 온라인 발급받는 방법과 가족관계증명서와의 차이, 필요서류를 안내합니다.",
        keywords="기본증명서 발급, 기본증명서 인터넷발급, 기본증명서 정부24, 기본증명서 상세",
        issuing_org="법원행정처(대법원)",
        online=True,
        online_desc="정부24 또는 전자가족관계등록시스템(efamily.scourt.go.kr)에서 본인 인증 후 무료로 즉시 발급됩니다.",
        offline_desc="주민센터 방문 또는 무인민원발급기에서 발급 가능합니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이(보통 발급 3개월 이내)",
        intro="기본증명서는 본인의 출생·사망·국적취득·개명·성별정정 등 신상에 관한 사항만을 증명하는 서류입니다. 가족관계증명서와 달리 다른 가족 구성원 정보는 나오지 않아, 본인 정보만 필요한 경우(개명 확인, 국적 확인 등)에 사용합니다.",
        notice="일반증명서에는 현재 유효한 정보만, 상세증명서에는 개명·국적변경 등 모든 이력이 표시됩니다.",
        uses=["개명 사실 확인", "국적 확인", "출생신고 확인", "각종 신원조회"],
        tips=[
            "가족관계증명서와 헷갈리기 쉬운데, 기본증명서는 '본인'에 대한 정보만 나온다는 점을 기억하세요.",
            "개명한 적이 있다면 상세증명서로 발급해야 이전 이름까지 확인할 수 있습니다.",
            "온라인 발급 화면에서 '일반'과 '상세' 선택란을 놓치지 마세요.",
        ],
        faqs=[
            ("기본증명서만으로 가족관계도 확인되나요?",
             "아니요. 기본증명서는 본인 신상 정보만 나오며 가족 구성원은 표시되지 않습니다. 가족관계가 필요하면 가족관계증명서를 별도로 발급받아야 합니다."),
            ("출생신고 직후에도 바로 발급되나요?",
             "출생신고가 시·구청 전산에 반영되는 데 통상 1~2일이 소요되며, 반영 후에는 온라인 발급이 가능합니다."),
            ("이 사이트에서 실제로 발급받을 수 있나요?",
             "아니요. 이 페이지는 발급 방법 안내만 제공하며, 실제 발급은 정부24 또는 전자가족관계등록시스템에서 진행하셔야 합니다."),
        ],
    ),
    dict(
        slug="marriage-cert", cat="family", emoji="💍",
        name="혼인관계증명서",
        title="혼인관계증명서 인터넷발급 방법·수수료 안내",
        desc="혼인관계증명서를 정부24에서 온라인으로 무료 발급받는 방법과 일반/상세 증명서 차이, 재혼 이력 표시 여부를 안내합니다.",
        keywords="혼인관계증명서 발급, 혼인관계증명서 인터넷발급, 혼인관계증명서 정부24",
        issuing_org="법원행정처(대법원)",
        online=True,
        online_desc="정부24 또는 전자가족관계등록시스템에서 본인 인증 후 무료 발급됩니다.",
        offline_desc="주민센터 방문 또는 무인민원발급기에서 발급 가능합니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이",
        intro="혼인관계증명서는 본인의 혼인·이혼 사실과 배우자 정보를 증명하는 서류입니다. 재혼, 국제결혼, 배우자 확인이 필요한 대출·보험·부동산 계약 등에서 요구됩니다.",
        notice="일반증명서에는 현재 배우자만, 상세증명서에는 이혼 이력을 포함한 과거 배우자 정보까지 모두 표시됩니다. 재혼 사실을 숨기고 싶어도 상세증명서를 요구받으면 전체 이력이 노출됩니다.",
        uses=["혼인 사실 증명", "배우자 확인(대출·보험)", "국제결혼 비자 신청", "이혼 사실 증명"],
        tips=[
            "국제결혼 비자 신청 시 상세증명서를 요구하는 경우가 많으니 미리 확인하세요.",
            "미혼인 경우에도 '혼인 사실 없음'이 표시된 증명서를 발급받을 수 있습니다.",
            "외국인 배우자와의 혼인은 혼인신고 처리 후 1~2일 뒤부터 증명서에 반영됩니다.",
        ],
        faqs=[
            ("미혼인데 혼인관계증명서를 발급받을 필요가 있나요?",
             "일부 금융·비자 절차에서 '혼인관계 없음'을 공식적으로 증명하기 위해 미혼자에게도 이 서류를 요구하는 경우가 있습니다."),
            ("이혼 사실이 일반증명서에도 나오나요?",
             "아니요. 일반증명서에는 현재 유효한 혼인관계만 표시되고, 이혼 이력은 상세증명서에만 나옵니다."),
            ("사실혼 관계도 증명되나요?",
             "아니요. 혼인관계증명서는 혼인신고가 접수된 법률혼만 증명하며 사실혼은 별도의 사실혼관계증명원(공증) 등 다른 방법으로 증명해야 합니다."),
        ],
    ),
    dict(
        slug="resident-register", cat="family", emoji="🏠",
        name="주민등록등본",
        title="주민등록등본 인터넷발급 방법·수수료·초본 차이 안내",
        desc="주민등록등본을 정부24에서 무료로 인터넷 발급받는 방법, 주민등록초본과의 차이, 세대주 확인 방법을 정리했습니다.",
        keywords="주민등록등본 발급, 주민등록등본 인터넷발급, 주민등록등본 정부24, 등본 초본 차이",
        issuing_org="행정안전부",
        online=True,
        online_desc="정부24에서 공동인증서·간편인증으로 본인 확인 후 무료로 즉시 발급·출력됩니다.",
        offline_desc="전국 모든 주민센터(주소지와 무관하게 가까운 곳 아무데나 방문 가능) 또는 무인민원발급기에서 발급 가능합니다.",
        fee_online="무료", fee_offline="무료(무인발급기), 400~500원(주민센터, 지자체별 상이)",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이(보통 1~3개월 이내 발급분 요구)",
        intro="주민등록등본은 세대주와 세대원 전원의 이름·주민등록번호·주소 이력을 보여주는 서류로, 전입세대 전원이 표시됩니다. 전세·대출 계약, 각종 정부지원 신청, 재직확인 등 세대 단위 확인이 필요한 거의 모든 절차에서 요구됩니다.",
        notice="주민등록번호 뒷자리, 과거 주소 이력 등 공개 범위를 온라인 발급 화면에서 직접 선택할 수 있습니다. 제출처가 요구하는 범위보다 과도하게 공개하지 않도록 확인 후 선택하세요.",
        uses=["전월세 계약", "대출 신청", "재직·재학 확인", "정부지원금 신청", "차량 등록"],
        tips=[
            "'세대주와의 관계'를 표시할지 여부를 선택할 수 있습니다 — 부동산 계약 시에는 보통 표시가 필요합니다.",
            "동거인·세대원이 여러 명이면 필요한 사람만 골라서 발급하는 '개별 열람' 옵션도 있습니다.",
            "온라인 발급 시 프린터가 없으면 PDF로 저장해 이메일로 제출해도 되는지 미리 제출처에 확인하세요.",
        ],
        faqs=[
            ("등본과 초본 중 뭘 발급받아야 하나요?",
             "세대원 전체 주소·구성을 보여주는 서류가 필요하면 등본, 본인 한 사람의 주소 변동 이력이 필요하면 초본을 발급받으세요. 계약서에 '등본' 또는 '초본'이라고 명시된 대로 발급하면 됩니다."),
            ("타 지역 주민센터에서도 발급되나요?",
             "네. 2007년부터 전국 어디서나 발급 가능한 '전국민원처리시스템'이 도입되어 주소지와 무관하게 가까운 주민센터에서 발급받을 수 있습니다."),
            ("세대원도 온라인으로 발급받을 수 있나요?",
             "세대주가 아닌 세대원도 본인 인증만 되면 온라인 발급이 가능합니다. 단, 세대주 정보 공개 범위는 세대주가 사전에 설정한 대로 제한될 수 있습니다."),
        ],
    ),
    dict(
        slug="resident-register-brief", cat="family", emoji="📋",
        name="주민등록초본",
        title="주민등록초본 인터넷발급 방법·수수료 안내",
        desc="주민등록초본을 정부24에서 무료로 발급받는 방법, 주소 변동 이력 공개 범위 설정법을 안내합니다.",
        keywords="주민등록초본 발급, 주민등록초본 인터넷발급, 주민등록초본 정부24",
        issuing_org="행정안전부",
        online=True,
        online_desc="정부24에서 본인 인증 후 무료로 즉시 발급됩니다.",
        offline_desc="전국 주민센터 또는 무인민원발급기에서 발급 가능합니다.",
        fee_online="무료", fee_offline="무료(무인발급기), 400~500원(주민센터)",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이",
        intro="주민등록초본은 본인 한 사람의 주소 변동 이력, 세대주 성명, 병역사항(선택) 등을 보여주는 서류입니다. 등본과 달리 다른 세대원 정보는 나오지 않아, 개인정보 노출을 최소화하면서 본인 이력만 증명할 때 사용합니다.",
        notice="주소 변동 이력을 '최근 주소만' 또는 '전체 이력'으로 선택할 수 있습니다. 병역사항·병력사항 표시 여부도 선택 가능하니 제출처 요구사항을 확인 후 설정하세요.",
        uses=["여권 재발급", "운전면허 갱신", "취업 서류 제출", "각종 신원조회", "해외 이주 신고"],
        tips=[
            "과거 주소 전체 이력이 필요한지, 현재 주소만 필요한지에 따라 발급 시 옵션을 다르게 선택하세요.",
            "해외 제출용은 번역공증이 필요할 수 있으니 미리 확인하세요.",
            "병역사항은 본인이 원할 때만 표시되도록 선택할 수 있습니다.",
        ],
        faqs=[
            ("초본에 과거 주소가 몇 년치까지 나오나요?",
             "발급 시 '전체 주소 이력' 또는 '최근 5년' 등으로 선택할 수 있어, 제출처가 요구하는 기간만큼만 발급받으면 됩니다."),
            ("본인이 아닌 가족의 초본도 발급받을 수 있나요?",
             "직계혈족(부모·자녀)은 일정 조건 하에 온라인으로 발급받을 수 있으나, 그 외 가족은 위임장을 지참해 방문 발급받아야 합니다."),
            ("영문 초본도 발급되나요?",
             "정부24에서 영문 주민등록표초본을 별도로 발급받을 수 있으며, 해외 비자·유학 서류로 주로 사용됩니다."),
        ],
    ),
    dict(
        slug="seal-cert", cat="family", emoji="🔴",
        name="인감증명서",
        title="인감증명서 발급 방법 — 인터넷발급 가능 여부·수수료 총정리",
        desc="인감증명서 인터넷발급이 가능한 경우와 방문이 필수인 경우(부동산·자동차 매도용, 법원·금융기관 제출용)를 정확히 구분해 안내합니다.",
        keywords="인감증명서 발급, 인감증명서 발급 인터넷, 인감증명서 인터넷발급, 인감증명서 방문, 인감증명서 수수료",
        issuing_org="행정안전부 / 읍·면·동 주민센터",
        online=True,
        online_desc="일반용(부동산·자동차 매도용이 아닌 용도)에 한해 정부24에서 공동인증서·금융인증서로 본인 인증 후 무료 발급됩니다. 2024년 하반기 제도 개편으로 온라인 발급이 새로 가능해졌습니다.",
        offline_desc="부동산·자동차 매도용이거나 법원·금융기관 제출용이라면 반드시 인감을 신고한 읍·면·동 주민센터를 방문해야 합니다(전국 아무 곳이 아닌 신고지 관할).",
        fee_online="무료", fee_offline="600원",
        docs=["신분증", "(대리 발급 시) 인감도장, 위임장, 대리인 신분증"],
        validity="제출처별 상이(보통 3개월 이내 발급분 요구)",
        intro="인감증명서는 사전에 등록해둔 인감(도장)이 본인 것임을 행정기관이 증명하는 서류로, 부동산 매매·자동차 매도·대출 보증 등 중요한 법률행위에서 요구됩니다. 2024년까지는 전량 방문 발급만 가능했으나, 이후 일반용에 한해 온라인 발급이 도입됐습니다.",
        notice="온라인 발급은 '일반용'만 가능합니다. 부동산 매도용, 자동차 매도용, 법원 제출용, 금융기관 제출용 인감증명서는 여전히 인감 신고지 주민센터를 직접 방문해야 발급받을 수 있습니다. 어떤 용도인지 모른다면 제출받는 기관에 먼저 확인하세요.",
        uses=["부동산 매매 계약", "자동차 매도", "대출·보증 계약", "법인 설립", "상속 협의분할"],
        tips=[
            "인감을 등록(신고)한 적이 없다면 먼저 주민센터에서 인감 신고부터 해야 발급받을 수 있습니다.",
            "온라인 발급 전, 제출처가 '일반용'을 받아주는지 반드시 먼저 확인하세요 — 잘못 발급하면 반려됩니다.",
            "본인서명사실확인서로 인감증명서를 대체할 수 있는 경우도 많으니, 인감도장이 없다면 이 대안도 검토해보세요.",
        ],
        faqs=[
            ("왜 인감증명서는 인터넷 발급이 제한적인가요?",
             "위조·도용 시 부동산 사기 등 재산상 피해가 크기 때문에, 정부는 신원 확인이 상대적으로 덜 중요한 '일반용'만 온라인 발급을 허용하고 고위험 용도는 대면 확인을 유지하고 있습니다."),
            ("인감증명서 대신 쓸 수 있는 서류가 있나요?",
             "본인서명사실확인서가 많은 경우 인감증명서를 대체할 수 있습니다. 인감도장을 분실했거나 새로 만들기 번거로우면 이 서류를 검토해보세요."),
            ("인감을 변경하려면 어떻게 하나요?",
             "인감 신고지 주민센터를 방문해 새 인감도장과 신분증을 지참하고 인감 변경 신고를 하면 됩니다."),
        ],
    ),
    dict(
        slug="signature-confirm-cert", cat="family", emoji="✍️",
        name="본인서명사실확인서",
        title="본인서명사실확인서 발급 방법 — 인감증명서 대체 가능 여부",
        desc="본인서명사실확인서를 정부24·주민센터에서 발급받는 방법과 인감증명서를 대체할 수 있는 경우를 안내합니다.",
        keywords="본인서명사실확인서 발급, 본인서명사실확인서 인터넷발급, 인감증명서 대체",
        issuing_org="행정안전부 / 읍·면·동 주민센터",
        online=True,
        online_desc="정부24에서 온라인 신청 후 방문 수령하거나, 사전 예약 후 주민센터에서 즉시 서명으로 발급받을 수 있습니다.",
        offline_desc="주민센터를 방문해 신분증을 제시하고 그 자리에서 서명하면 담당 공무원이 서명 사실을 확인해 발급합니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증"],
        validity="제출처별 상이",
        intro="본인서명사실확인서는 인감도장 대신 '서명'이 본인 것임을 행정기관이 확인해주는 서류입니다. 2012년 도입된 제도로, 인감도장을 파거나 등록할 필요 없이 신분증만 있으면 발급받을 수 있어 인감증명서의 대안으로 널리 쓰입니다.",
        notice="모든 인감증명서 용도를 대체하지는 못합니다. 부동산 매도용 등 일부 절차는 여전히 인감증명서만 인정하는 경우가 있으니, 제출처에 본인서명사실확인서 인정 여부를 먼저 확인하세요.",
        uses=["계약서 서명 확인", "인감증명서 대체", "각종 동의서 제출"],
        tips=[
            "인감도장이 없거나 잃어버렸다면 인감을 새로 만들지 않고 이 서류로 대체할 수 있는지 먼저 확인해보세요.",
            "온라인 신청 후에도 최초 1회는 반드시 본인이 직접 주민센터를 방문해 서명해야 합니다(전자서명 불가).",
            "전자본인서명확인서 형태로 발급받으면 재방문 없이 필요할 때마다 재발급받을 수 있습니다.",
        ],
        faqs=[
            ("인감증명서와 완전히 동일한 효력이 있나요?",
             "본인서명사실확인서 등에 관한 법률에 따라 인감증명서와 같은 효력을 가지지만, 일부 기관이나 계약에서는 관행적으로 인감증명서만 요구하는 경우가 있어 사전 확인이 필요합니다."),
            ("전자본인서명확인서는 무엇이 다른가요?",
             "최초 1회 주민센터 방문 후 발급받는 '전자본인서명확인서 발급증'의 확인번호로, 이후에는 정부24에서 방문 없이 재발급받을 수 있는 서비스입니다."),
            ("이 사이트에서 실제로 발급받을 수 있나요?",
             "아니요. 이 페이지는 절차 안내만 제공하며, 실제 발급·서명은 정부24 신청 후 주민센터에서 진행됩니다."),
        ],
    ),
    dict(
        slug="income-cert", cat="tax", emoji="💰",
        name="소득금액증명원",
        title="소득금액증명원 인터넷발급 방법 — 홈택스·정부24 무료 발급",
        desc="소득금액증명원을 홈택스에서 무료로 발급받는 방법, 종합소득세 신고 전에도 발급 가능한지, 소득 없음 증명서와의 차이를 안내합니다.",
        keywords="소득금액증명원 발급, 소득금액증명원 인터넷발급, 소득금액증명원 홈택스, 소득금액증명원 정부24",
        issuing_org="국세청(홈택스)",
        online=True,
        online_desc="국세청 홈택스(hometax.go.kr) 또는 정부24에서 공동인증서·간편인증으로 로그인 후 무료로 즉시 발급됩니다. 손택스(모바일 앱)에서도 발급 가능합니다.",
        offline_desc="세무서를 방문해 신분증을 제시하면 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이(주로 최근 발급분 요구)",
        intro="소득금액증명원은 국세청에 신고된 연간 종합소득금액(근로·사업·기타소득 등)을 증명하는 서류로, 대출 심사·전세자금대출·정부지원금 신청·비자 발급 등 소득 확인이 필요한 거의 모든 절차에서 요구됩니다.",
        notice="당해연도 소득은 다음 해 5~6월 종합소득세 확정신고·정산이 끝나야 반영됩니다. 신고 전 기간에는 직전 연도 소득만 조회·발급되니 시점을 확인하세요. 소득이 없다면 '사실증명(소득금액증명 발급불가)' 또는 '소득없음 사실확인' 서류로 대체됩니다.",
        uses=["대출·전세자금대출 심사", "정부지원금·건강보험료 산정", "비자 신청", "국민연금 임의가입"],
        tips=[
            "프리랜서·사업소득자는 5월 종합소득세 신고를 마쳐야 최신 소득으로 발급됩니다 — 신고 전이라면 이 점을 미리 은행 등에 안내하세요.",
            "근로소득만 있는 직장인은 연말정산 이후(2월경) 전년도 소득이 반영됩니다.",
            "소득이 아예 없는 경우 '소득금액증명(소득없음)'으로 발급되며, 이 역시 정식 증빙 서류로 인정됩니다.",
        ],
        faqs=[
            ("올해 번 돈이 왜 증명서에 안 나오나요?",
             "국세청 소득 데이터는 다음 해 종합소득세 신고·정산이 완료된 이후에 반영됩니다. 즉 2026년 소득은 2027년 5~6월 신고 이후에야 소득금액증명원에 나타납니다."),
            ("아르바이트생도 발급받을 수 있나요?",
             "네. 원천징수된 소득이 국세청에 신고되어 있다면 아르바이트·일용직 소득도 조회·발급됩니다."),
            ("무소득자도 발급이 필요한가요?",
             "기초생활수급 신청, 건강보험 피부양자 등록 등에서 '소득 없음'을 공식 증명하기 위해 무소득자도 이 서류를 요구받는 경우가 많습니다."),
        ],
    ),
    dict(
        slug="local-tax-cert", cat="tax", emoji="🏛️",
        name="지방세 납세증명서",
        title="지방세 납세증명서 인터넷발급 방법 — 위택스·정부24 무료",
        desc="지방세 납세증명서(완납증명)를 위택스·정부24에서 무료로 발급받는 방법과 체납이 있을 때 발급 가능 여부를 안내합니다.",
        keywords="지방세 납세증명서 발급, 지방세완납증명서 발급, 위택스 납세증명서, 정부24 지방세증명",
        issuing_org="행정안전부(위택스) / 지방자치단체",
        online=True,
        online_desc="위택스(wetax.go.kr) 또는 정부24에서 공동인증서·간편인증으로 로그인 후 무료로 즉시 발급됩니다.",
        offline_desc="관할 구청·시청 세무과를 방문해 신분증을 제시하면 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="발급일로부터 통상 30일",
        intro="지방세 납세증명서는 재산세·자동차세·주민세 등 지방세를 체납하지 않고 성실히 납부했음을 증명하는 서류입니다. 정부 입찰 참가, 인허가 신청, 대출, 관급공사 계약 등에서 흔히 요구됩니다.",
        notice="체납액이 있으면 원칙적으로 발급되지 않습니다. 완납 후 즉시 재조회하면 발급 가능한 경우가 많으니, 급하게 필요하다면 미납 세금부터 납부하세요.",
        uses=["정부 입찰·인허가 신청", "대출 심사", "출국금지 여부 확인", "각종 정부지원 신청"],
        tips=[
            "국세 납세증명서와는 별개의 서류입니다 — 발급 기관과 요구 서류를 잘 구분하세요.",
            "체납 사실이 있으면 위택스에서 바로 납부 후 몇 분 내로 재조회·발급이 가능합니다.",
            "여러 지자체에 걸쳐 세금을 낸 경우에도 위택스에서 통합 조회·발급됩니다.",
        ],
        faqs=[
            ("국세 완납증명서와 뭐가 다른가요?",
             "지방세 납세증명서는 재산세·자동차세 등 '지방세', 국세 납세증명서는 소득세·부가가치세 등 '국세'의 완납 여부를 증명합니다. 제출처가 요구하는 종류를 정확히 확인하세요."),
            ("체납액이 있으면 아예 발급이 안 되나요?",
             "원칙적으로 발급되지 않지만, 지자체별로 소액체납이거나 납부 유예 중인 경우 예외적으로 발급되는 경우도 있어 관할 세무과에 문의하는 것이 정확합니다."),
            ("법인도 발급받을 수 있나요?",
             "네. 법인 명의로 위택스에 가입하면 법인의 지방세 납세증명서도 온라인으로 발급받을 수 있습니다."),
        ],
    ),
    dict(
        slug="national-tax-cert", cat="tax", emoji="🧾",
        name="국세 납세증명서",
        title="국세 납세증명서(완납증명) 인터넷발급 방법 — 홈택스 무료",
        desc="국세 납세증명서를 홈택스에서 무료로 발급받는 방법과 체납 시 발급 가능 여부, 지방세 납세증명서와의 차이를 안내합니다.",
        keywords="국세 납세증명서 발급, 국세완납증명서 발급, 홈택스 납세증명서, 국세증명 인터넷발급",
        issuing_org="국세청(홈택스)",
        online=True,
        online_desc="홈택스(hometax.go.kr) 또는 정부24에서 공동인증서·간편인증 로그인 후 무료로 즉시 발급됩니다.",
        offline_desc="세무서를 방문해 신분증을 제시하면 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="발급일로부터 통상 30일",
        intro="국세 납세증명서는 소득세·법인세·부가가치세 등 국세를 체납하지 않았음을 증명하는 서류로, 정부 계약·입찰, 인허가, 비자 신청, 대출 심사 등에서 요구됩니다.",
        notice="체납액이 있으면 원칙적으로 발급이 제한됩니다. 단, 징수유예·체납처분유예 중이거나 소액체납인 경우 예외적으로 발급될 수 있으니 관할 세무서에 확인하세요.",
        uses=["정부 입찰·계약", "인허가 신청", "비자 신청", "대출 심사"],
        tips=[
            "지방세 납세증명서와 헷갈리지 마세요 — 국세청이 아닌 위택스에서 발급하는 것은 지방세용입니다.",
            "사업자는 사업자용, 개인은 개인용으로 각각 발급받아야 하는 경우가 있으니 제출처 요구사항을 확인하세요.",
            "홈택스 모바일 앱(손택스)에서도 동일하게 발급 가능합니다.",
        ],
        faqs=[
            ("사업자와 개인 중 어떤 걸로 발급받아야 하나요?",
             "제출 목적에 따라 다릅니다. 개인 명의 대출이면 개인 납세증명서, 사업 관련 계약·입찰이면 사업자 납세증명서를 발급받으세요."),
            ("연대납세의무자도 확인되나요?",
             "네. 홈택스에서 본인 명의뿐 아니라 연대납세의무 관련 체납 여부도 함께 조회됩니다."),
            ("발급 즉시 유효한가요?",
             "네, 조회 시점 기준으로 발급되며 통상 발급일로부터 30일간 유효한 것으로 인정받습니다(제출처마다 상이할 수 있음)."),
        ],
    ),
    dict(
        slug="health-insurance-cert", cat="insurance", emoji="🏥",
        name="건강보험자격득실확인서",
        title="건강보험자격득실확인서 발급 방법 — 국민건강보험공단·정부24 무료",
        desc="건강보험자격득실확인서를 국민건강보험공단 홈페이지·정부24·모바일앱·팩스로 무료 발급받는 방법을 안내합니다.",
        keywords="건강보험자격득실확인서 발급, 건강보험자격득실확인서 인터넷발급, 자격득실확인서 정부24, 건강보험자격득실확인서 발급 정부24",
        issuing_org="국민건강보험공단",
        online=True,
        online_desc="국민건강보험공단 홈페이지(nhis.or.kr), 정부24, 모바일 앱 '건강보험 25시'에서 공동인증서·간편인증 로그인 후 무료로 즉시 발급됩니다. 무인민원발급기에서도 가능합니다.",
        offline_desc="가까운 국민건강보험공단 지사를 방문하면 무료로 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이",
        intro="건강보험자격득실확인서는 건강보험 가입·상실 이력(직장가입자/지역가입자 구분, 가입 기간)을 증명하는 서류로, 이직 시 4대보험 취득·상실 확인, 실업급여 신청, 대출 심사 등에서 흔히 요구됩니다.",
        notice="65세 이상이거나 등록 장애인은 고객센터(1577-1000) 상담사를 통한 디지털ARS 팩스 발급도 가능해 인터넷이 어려운 경우에도 이용할 수 있습니다.",
        uses=["이직 시 4대보험 취득·상실 확인", "실업급여 신청", "대출 심사", "재직 확인"],
        tips=[
            "직장을 옮긴 직후라면 새 직장의 자격취득 신고가 처리된 뒤 발급하는 것이 정확합니다(통상 1~2일 소요).",
            "모바일 앱 '건강보험 25시'를 설치해두면 다음에는 앱에서 바로 발급받을 수 있어 편리합니다.",
            "가입기간 전체가 필요한지 최근 이력만 필요한지 확인 후 조회 기간을 설정하세요.",
        ],
        faqs=[
            ("직장가입자와 지역가입자 이력이 모두 나오나요?",
             "네. 최초 가입일부터 현재까지 직장가입자·지역가입자 전환 이력이 모두 표시됩니다."),
            ("퇴사 직후 바로 발급되나요?",
             "퇴사 처리(자격상실 신고)가 공단 전산에 반영된 이후 발급 가능하며, 통상 퇴사일 기준 며칠 내로 반영됩니다."),
            ("팩스로도 받을 수 있나요?",
             "네. 디지털ARS를 통해 팩스 발급이 가능하며, 만 65세 이상이거나 등록 장애인은 고객센터 상담사를 통해서도 팩스로 받을 수 있습니다."),
        ],
    ),
    dict(
        slug="pension-cert", cat="insurance", emoji="👵",
        name="국민연금가입증명서",
        title="국민연금가입증명서 발급 방법 — 국민연금공단·정부24 무료",
        desc="국민연금가입증명서를 국민연금공단 홈페이지·정부24에서 무료로 발급받는 방법과 가입내역확인서와의 차이를 안내합니다.",
        keywords="국민연금가입증명서 발급, 국민연금가입증명서 인터넷발급, 국민연금 정부24, 국민연금 가입내역확인서",
        issuing_org="국민연금공단",
        online=True,
        online_desc="국민연금공단 홈페이지(nps.or.kr) 또는 정부24에서 공동인증서·간편인증 로그인 후 무료로 즉시 발급됩니다.",
        offline_desc="가까운 국민연금공단 지사를 방문하면 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이",
        intro="국민연금가입증명서는 국민연금 가입 여부와 가입 기간을 증명하는 서류로, 대출 심사·재직 확인·경력 증빙(회사가 폐업해 재직증명서를 받을 수 없을 때 대체 자료로도 활용) 등에 쓰입니다.",
        notice="유사 서류로 '국민연금 가입내역확인서'가 있는데, 이는 월별 납부 보험료·소득월액까지 상세히 나오는 서류입니다. 단순 가입 여부만 필요한지, 상세 납부 내역까지 필요한지에 따라 골라서 발급받으세요.",
        uses=["대출 심사", "재직·경력 증빙(폐업 회사 대체 자료)", "실업급여 신청 보조자료"],
        tips=[
            "폐업한 회사의 경력을 증빙해야 한다면 국민연금가입내역확인서가 재직증명서의 대안이 될 수 있습니다.",
            "임의가입자(전업주부 등)도 가입 이력이 있다면 동일하게 발급받을 수 있습니다.",
            "영문 증명서도 발급 가능해 해외 이주·비자 신청에 활용할 수 있습니다.",
        ],
        faqs=[
            ("가입증명서와 가입내역확인서 중 뭘 받아야 하나요?",
             "단순히 '가입했다는 사실'만 필요하면 가입증명서, 월별 납부액까지 상세히 필요하면 가입내역확인서를 발급받으세요."),
            ("연금 수령액도 이 서류에 나오나요?",
             "아니요. 가입증명서는 가입 여부·기간만 나오며, 예상 연금액은 국민연금공단의 '내 연금 알아보기' 서비스에서 별도로 조회해야 합니다."),
            ("납부예외 기간도 표시되나요?",
             "네. 실업·휴직 등으로 보험료를 내지 않은 납부예외 기간도 가입내역확인서에 구분되어 표시됩니다."),
        ],
    ),
    dict(
        slug="employment-insurance-cert", cat="insurance", emoji="💼",
        name="고용보험 피보험자격이력내역서",
        title="고용보험 피보험자격이력내역서 발급 방법 — 고용보험 홈페이지·정부24 무료",
        desc="고용보험 피보험자격이력내역서를 고용보험 홈페이지·정부24에서 무료로 발급받는 방법과 실업급여 신청 시 활용법을 안내합니다.",
        keywords="고용보험 피보험자격이력내역서 발급, 고용보험 이력내역서 인터넷발급, 고용보험 정부24, 실업급여 이력내역서",
        issuing_org="근로복지공단 / 고용노동부",
        online=True,
        online_desc="고용보험 홈페이지(ei.go.kr) 또는 정부24에서 공동인증서·간편인증 로그인 후 무료로 즉시 발급됩니다.",
        offline_desc="가까운 고용센터를 방문하면 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이",
        intro="고용보험 피보험자격이력내역서는 근무했던 사업장별 고용보험 취득·상실일과 근무 기간을 모두 보여주는 서류로, 실업급여(구직급여) 신청, 경력 증빙, 폐업한 회사의 재직 이력 확인 등에 필수적으로 사용됩니다.",
        notice="사업장별로 상실 사유(자진퇴사/권고사직/계약만료 등)가 코드로 표시됩니다. 실업급여 수급 자격은 상실 사유에 따라 달라지므로, 신청 전 이 서류로 미리 사유 코드를 확인해두면 좋습니다.",
        uses=["실업급여(구직급여) 신청", "경력 증빙", "폐업 회사 재직 이력 확인", "이직확인서 처리 확인"],
        tips=[
            "실업급여를 신청하려면 퇴사한 회사가 '이직확인서'를 고용센터에 제출 완료했는지부터 이 서류로 확인하세요.",
            "여러 직장을 옮겨 다녔다면 전체 이력이 한 번에 표시되어 경력 증빙용으로도 편리합니다.",
            "상실 사유 코드가 실제와 다르게 기재됐다면 회사에 정정을 요청해야 실업급여 수급에 불이익이 없습니다.",
        ],
        faqs=[
            ("실업급여 신청에 이 서류가 꼭 필요한가요?",
             "고용센터 담당자가 전산으로 직접 조회하는 경우가 많아 필수 제출서류는 아니지만, 상실 사유가 정확히 반영됐는지 본인이 미리 확인하는 용도로 유용합니다."),
            ("이직확인서와는 다른 서류인가요?",
             "네. 이직확인서는 회사가 고용센터에 제출하는 서류이고, 피보험자격이력내역서는 근로자 본인이 그 처리 결과를 확인하는 서류입니다."),
            ("프리랜서·특수고용직도 발급받을 수 있나요?",
             "고용보험에 가입된 이력이 있는 경우(2021년 이후 예술인·노무제공자 고용보험 확대 적용 등)에는 동일하게 조회·발급됩니다."),
        ],
    ),
    dict(
        slug="criminal-record-cert", cat="military", emoji="🚔",
        name="범죄경력회보서",
        title="범죄경력회보서(범죄사실확인서) 발급 방법 — 경찰청 온라인 발급시스템",
        desc="범죄경력회보서를 경찰청 발급시스템·정부24에서 온라인으로 무료 발급받는 방법과 유효기간(6개월), 취업목적 발급 시 주의사항을 안내합니다.",
        keywords="범죄경력회보서 발급, 범죄경력회보서 인터넷발급, 범죄경력회보서 정부24, 범죄경력조회 발급",
        issuing_org="경찰청",
        online=True,
        online_desc="경찰청 범죄경력회보서 발급시스템(crims.police.go.kr) 또는 정부24에서 24시간 온라인으로 무료 발급받을 수 있습니다.",
        offline_desc="주소지 관할 경찰서 민원실을 방문해 신분증을 제시하면 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증"],
        validity="발급일로부터 6개월",
        intro="범죄경력회보서(과거 범죄경력증명서)는 본인의 범죄경력·수사경력 유무를 공식 증명하는 서류입니다. 2024년 2월 명칭이 개편되었으며, 채용, 어린이집·학교 등 아동·청소년 관련 기관 취업, 해외 이민·비자 신청 등에서 요구됩니다.",
        notice="발급 목적에 따라 처리 방식이 다릅니다. 본인 확인용은 신청 즉시 출력되지만, 아동·청소년기관 취업 등 법령상 회보 대상 기관에 직접 통보되는 경우는 처리에 2~3일이 걸릴 수 있습니다. 유효기간은 발급일로부터 6개월이므로 미리 발급해두지 마세요.",
        uses=["아동·청소년 관련 기관 취업(어린이집·학교 등)", "해외 이민·비자 신청", "특정 자격증 취득", "공무원 임용"],
        tips=[
            "유효기간이 6개월로 짧으니 제출 시점에 맞춰 발급받으세요.",
            "취업 목적으로 회사가 직접 요구하는 경우, 본인이 발급받은 서류를 제출하는 방식인지 기관 간 직접 통보 방식인지 미리 확인하세요.",
            "본인 확인용은 즉시 출력되지만 법정 의무 조회 대상 업종은 처리 기간이 있을 수 있어 여유 있게 신청하세요.",
        ],
        faqs=[
            ("범죄경력증명서와 이름이 다른데 같은 서류인가요?",
             "네. 2024년 2월 13일부터 기존 '범죄경력증명서'가 '범죄·수사경력회보서'로 명칭이 변경되었을 뿐 같은 서류입니다."),
            ("실효된(사면·기간경과) 전과도 나오나요?",
             "형의 실효 등에 관한 법률에 따라 일정 기간이 지나 실효된 형은 원칙적으로 표시되지 않습니다."),
            ("타인이 대신 발급받을 수 있나요?",
             "온라인은 본인 인증이 필요해 대리 발급이 불가능합니다. 위임장과 대리인 신분증을 지참하면 경찰서 방문 대리 발급이 가능한 경우가 있으니 관할 경찰서에 문의하세요."),
        ],
    ),
    dict(
        slug="military-service-cert", cat="military", emoji="🎖️",
        name="병적증명서",
        title="병적증명서 인터넷발급 방법 — 병무청·정부24 무료",
        desc="병적증명서를 병무청 홈페이지·정부24에서 무료로 온라인 발급받는 방법과 전역 후 발급 가능 시점, 대리 발급 여부를 안내합니다.",
        keywords="병적증명서 발급, 병적증명서 인터넷발급, 병적증명서 정부24, 병무청 병적증명서",
        issuing_org="병무청",
        online=True,
        online_desc="병무청 홈페이지(mma.go.kr) 또는 정부24에서 공동인증서·간편인증(카카오·PASS 등) 로그인 후 무료로 발급받을 수 있습니다. 모바일 신청은 가능하지만 출력은 PC에서만 됩니다.",
        offline_desc="가까운 지방병무청·주민센터를 방문하면 발급받을 수 있습니다.",
        fee_online="무료", fee_offline="무료",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이",
        intro="병적증명서는 현역 복무, 보충역, 병역면제, 병역미필 등 병역이행 사항을 상세히 증명하는 서류로, 공무원 임용, 취업, 이민·비자 심사 등 병역 확인이 필요한 절차에서 요구됩니다.",
        notice="전역 후 최소 1개월이 지나야 전역 정보가 반영되어 발급 가능합니다. 병역면제자는 1989년 1월 1일 이후 병역판정검사를 받은 경우에만 온라인 발급 대상입니다. 인터넷 발급은 대리 발급이 불가능합니다(방문 시 위임장 지참하면 가능).",
        uses=["공무원 임용", "취업(병역 확인)", "이민·비자 심사", "각종 신원조회"],
        tips=[
            "전역 직후 급하게 필요하다면 1개월 반영 기간을 고려해 미리 일정을 조정하세요.",
            "모바일에서 신청까지는 되지만 출력은 PC로만 가능하니 PC 환경에서 최종 출력하세요.",
            "여러 통이 필요하면 한 번에 여러 부를 신청해 출력할 수 있습니다.",
        ],
        faqs=[
            ("현역 복무 중에도 발급받을 수 있나요?",
             "복무 중에도 현재까지의 병적 사항으로 발급받을 수 있습니다."),
            ("여성도 발급받을 수 있나요?",
             "지원에 의해 현역·부사관 등으로 복무한 여성은 해당 이력에 대해 발급받을 수 있으며, 병역의무가 없는 여성은 원칙적으로 발급 대상이 아닙니다."),
            ("병역면제 사유도 상세히 나오나요?",
             "네. 신체등위, 면제 사유 등이 증명서에 코드 또는 문구로 표시됩니다."),
        ],
    ),
    dict(
        slug="graduation-cert", cat="edu", emoji="🎓",
        name="졸업증명서",
        title="졸업증명서 인터넷발급 방법 — 정부24 무료 발급 대상 학교 확인",
        desc="졸업증명서를 정부24에서 무료로 발급받는 방법과 정부24 미지원 학교의 경우 학교 직접 신청 방법을 안내합니다.",
        keywords="졸업증명서 발급, 졸업증명서 인터넷발급, 졸업증명서 정부24, 졸업증명서 무료발급",
        issuing_org="교육부(정부24) / 각급 학교",
        online=True,
        online_desc="초·중·고등학교와 정부24와 연계된 대학은 정부24에서 무료로 즉시 발급됩니다. 연계되지 않은 대학·대학원은 학교 홈페이지의 증명서 발급 시스템(대부분 '더원', '이지웰' 등 위탁업체 이용)에서 별도 발급받아야 합니다.",
        offline_desc="졸업한 학교 행정실·학사지원팀을 방문하거나 우편으로 신청할 수 있습니다.",
        fee_online="무료(정부24) 또는 500~1,000원(학교 자체 시스템)",
        fee_offline="500~1,000원(학교별 상이)",
        docs=["신분증(방문 시)"],
        validity="제출처별 상이",
        intro="졸업증명서는 특정 학교의 특정 과정을 졸업했음을 증명하는 서류로, 입사 지원, 편입학, 자격증 응시자격 확인, 공무원 임용 등에서 요구됩니다.",
        notice="모든 대학이 정부24와 연계된 것은 아닙니다. 정부24에서 학교 검색이 안 되면 해당 학교 홈페이지의 '증명서 발급' 메뉴(외부 위탁 시스템으로 연결되는 경우가 많음)에서 직접 발급받아야 합니다. 폐교된 학교는 관할 교육청이나 통합 관리 대학에 문의해야 합니다.",
        uses=["입사 지원", "편입학·대학원 진학", "자격증 응시자격 확인", "공무원 임용"],
        tips=[
            "정부24에서 학교명이 검색되지 않으면 학교 자체 홈페이지의 증명서 발급 코너를 확인하세요.",
            "영문 졸업증명서가 필요한 해외 유학·이민의 경우 학교에 영문 증명서 발급이 가능한지 별도로 문의해야 합니다.",
            "폐교된 학교 졸업생은 관할 시·도 교육청 또는 통합 관리 기관에 문의하면 발급 경로를 안내받을 수 있습니다.",
        ],
        faqs=[
            ("모든 대학이 정부24에서 발급되나요?",
             "아니요. 정부24와 전자적으로 연계된 학교만 가능하며, 연계되지 않은 학교는 학교 자체 증명서 발급 시스템을 이용해야 합니다."),
            ("성적증명서도 같은 방법으로 발급되나요?",
             "네. 정부24 연계 학교라면 졸업증명서와 같은 화면에서 성적증명서도 함께 발급받을 수 있습니다."),
            ("재학 중인데 졸업예정증명서가 필요해요.",
             "졸업예정증명서는 정부24가 아닌 재학 중인 학교의 행정실·학사지원팀에서 별도로 발급받아야 하는 경우가 많습니다."),
        ],
    ),
    dict(
        slug="real-estate-register", cat="estate", emoji="🏘️",
        name="부동산 등기부등본",
        title="부동산 등기부등본(등기사항전부증명서) 인터넷발급 방법·수수료",
        desc="부동산 등기부등본을 인터넷등기소에서 발급받는 방법과 수수료(열람 700원, 발급 1,000원), 말소사항 포함 여부를 안내합니다.",
        keywords="등기부등본 발급, 등기부등본 인터넷발급, 등기부등본 열람, 등기사항전부증명서 발급",
        issuing_org="법원행정처(인터넷등기소)",
        online=True,
        online_desc="대법원 인터넷등기소(iros.go.kr)에서 주소나 소유자명으로 검색 후 결제하면 즉시 열람·출력할 수 있습니다. 로그인 없이도 발급 가능합니다.",
        offline_desc="전국 등기소(등기과)를 방문하면 발급받을 수 있습니다.",
        fee_online="열람 700원 / 발급(출력) 1,000원", fee_offline="발급 1,200원",
        docs=["없음(누구나 발급 가능, 익명 열람 지원)"],
        validity="발급일 기준 현재 상태를 증명(실시간성이 중요해 오래된 등기부등본은 잘 인정되지 않음)",
        intro="부동산 등기부등본(정식 명칭: 등기사항전부증명서)은 해당 부동산의 소유자, 근저당권·전세권 등 권리관계 전체를 보여주는 서류입니다. 전세·매매 계약 전 반드시 확인해야 하는 필수 서류로, 신분증이나 이해관계 증명 없이 주소만 알면 누구나 열람·발급받을 수 있습니다.",
        notice="계약 직전에 반드시 '말소사항 포함'으로 발급해 과거 근저당이 실제로 말소됐는지까지 확인하세요. 계약금을 입금하기 직전 재발급해 그 사이 권리관계가 바뀌지 않았는지 재확인하는 것이 안전합니다.",
        uses=["전세·매매 계약 전 권리관계 확인", "대출 심사", "경매 참여 검토"],
        tips=[
            "계약 당일에도 잔금 지급 직전 다시 한번 발급받아 근저당 설정 등 변동이 없는지 재확인하세요.",
            "'말소사항 포함'으로 발급하면 과거에 설정됐다가 없어진 권리까지 모두 확인할 수 있어 더 안전합니다.",
            "집합건물(아파트 등)은 표제부에 대지권 비율까지 함께 확인하세요.",
        ],
        faqs=[
            ("소유자 본인이 아니어도 발급받을 수 있나요?",
             "네. 등기부등본은 공시 제도의 특성상 누구나 주소만 알면 열람·발급받을 수 있습니다."),
            ("열람과 발급(출력)의 차이는 무엇인가요?",
             "열람은 화면으로만 보는 것으로 법적 효력이 없는 참고용이고, 발급(출력)은 법원 직인이 찍힌 정식 증명서로 공적 효력이 있습니다."),
            ("등기부등본과 건축물대장은 같은 건가요?",
             "아닙니다. 등기부등본은 '권리관계'(소유자·근저당 등)를, 건축물대장은 '건물 자체의 물리적 현황'(구조·면적·용도)을 보여줍니다. 계약 전에는 두 서류를 함께 확인하는 것이 안전합니다."),
        ],
    ),
    dict(
        slug="passport", cat="travel", emoji="🛂",
        name="여권 발급·재발급",
        title="여권 재발급 인터넷 신청 방법 2026 — 수수료·유효기간·소요기간",
        desc="여권 재발급을 정부24에서 온라인 신청하는 방법과 수수료(10년 복수여권 53,000원), 최초 발급 시 방문이 필요한 이유를 안내합니다.",
        keywords="여권 발급, 여권 재발급, 여권 재발급 인터넷신청, 여권 발급 수수료, 여권 발급 정부24",
        issuing_org="외교부",
        online=True,
        online_desc="이전에 여권을 발급받은 적이 있는 성인(만 18세 이상)이라면 정부24에서 사진 업로드·수수료 결제까지 온라인으로 신청할 수 있습니다. 단, 수령은 반드시 지정한 구청·시청 여권과를 방문해야 합니다.",
        offline_desc="생애 최초 발급자, 개명한 경우, 만 18세 미만 미성년자는 온라인 신청이 불가능해 반드시 구청·시청 여권과를 방문해 신청해야 합니다.",
        fee_online="10년 복수여권 53,000원 / 5년 복수여권(18세 미만) 45,000원",
        fee_offline="동일(신청 방식과 무관하게 여권 종류별 수수료는 같음)",
        docs=["여권용 사진(6개월 이내 촬영)", "신분증", "(미성년자) 기본증명서·가족관계증명서 등"],
        validity="10년(성인) / 5년(18세 미만)",
        intro="여권은 해외 출국 시 신분을 증명하는 필수 서류입니다. 정부24 온라인 재발급 서비스 도입으로 재발급 대상자는 방문 없이 신청 후 수령만 하면 되지만, 최초 발급자나 미성년자는 여전히 전 과정을 방문해야 합니다.",
        notice="온라인 신청 후 발급까지 통상 7~10일이 소요되므로 출국일이 임박했다면 여유 있게 신청하세요. 여권 사진은 규격(가로 3.5cm×세로 4.5cm, 6개월 이내 촬영, 무배경)을 지키지 않으면 반려될 수 있습니다.",
        uses=["해외 출국", "해외 비자 신청", "국제 신분증명"],
        tips=[
            "출국 임박 시 서울 지역은 신속 여권 발급 서비스(당일~2일)를 이용할 수 있는지 확인하세요.",
            "온라인 신청이라도 수령은 본인이 직접 방문해야 하니, 신청 시 수령 가능한 구청을 정확히 지정하세요.",
            "미성년 자녀 여권은 법정대리인이 동반해 방문 신청해야 하는 경우가 많습니다.",
        ],
        faqs=[
            ("모든 사람이 온라인으로 재발급받을 수 있나요?",
             "만 18세 이상이면서 이전에 여권을 발급받은 적이 있고, 개명 등으로 인적사항이 바뀌지 않은 경우에만 온라인 신청이 가능합니다."),
            ("여권 사진을 어떻게 온라인으로 제출하나요?",
             "정부24 신청 화면에서 규격에 맞는 사진 파일을 업로드하면 되며, 사진관에서 '여권용 디지털 파일'로 요청하면 규격에 맞게 받을 수 있습니다."),
            ("분실했을 때도 재발급 방식이 같나요?",
             "분실 신고 후 재발급 신청 시에는 분실 경위서 등 추가 서류가 필요할 수 있어 원칙적으로 방문 신청을 권장합니다."),
        ],
    ),
]


# slug -> (사이트명, 발급 사이트 URL) — 온라인 발급 CTA 버튼용
ONLINE_SITES = {
    "family-relation-cert": ("정부24", "https://www.gov.kr"),
    "basic-cert": ("정부24", "https://www.gov.kr"),
    "marriage-cert": ("정부24", "https://www.gov.kr"),
    "resident-register": ("정부24", "https://www.gov.kr"),
    "resident-register-brief": ("정부24", "https://www.gov.kr"),
    "seal-cert": ("정부24", "https://www.gov.kr"),
    "signature-confirm-cert": ("정부24", "https://www.gov.kr"),
    "income-cert": ("홈택스", "https://www.hometax.go.kr"),
    "local-tax-cert": ("위택스", "https://www.wetax.go.kr"),
    "national-tax-cert": ("홈택스", "https://www.hometax.go.kr"),
    "health-insurance-cert": ("국민건강보험공단", "https://www.nhis.or.kr"),
    "pension-cert": ("국민연금공단", "https://www.nps.or.kr"),
    "employment-insurance-cert": ("고용보험 홈페이지", "https://www.ei.go.kr"),
    "criminal-record-cert": ("경찰청 범죄경력회보서 발급시스템", "https://crims.police.go.kr"),
    "military-service-cert": ("병무청", "https://www.mma.go.kr"),
    "graduation-cert": ("정부24", "https://www.gov.kr"),
    "real-estate-register": ("인터넷등기소", "https://www.iros.go.kr"),
    "passport": ("정부24", "https://www.gov.kr"),
}


def kakao_naver_style_notice():
    return "이 페이지는 정부기관 공식 절차를 바탕으로 정리한 안내 콘텐츠이며, 실제 발급은 각 공식 사이트 또는 방문 기관에서 진행됩니다. 제도는 수시로 바뀔 수 있으니 중요한 절차는 발급 직전 해당 기관 공지사항으로 다시 확인하세요."


HEAD_COMMON = """<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-9ZGENFSXWC"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-9ZGENFSXWC');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6464921081676309" crossorigin="anonymous"></script>
<meta name="theme-color" content="#2563EB">
"""

HEADER_TMPL = """<header>
  <div class="header-inner">
    <a href="{root}index.html" class="logo">WooaCert</a>
    <nav>
      <a href="{root}index.html#family">가족·신분</a>
      <a href="{root}index.html#tax">세금·소득</a>
      <a href="{root}index.html#insurance">4대보험</a>
      <a href="{root}index.html#military">병역·범죄</a>
      <a href="{root}index.html#estate">부동산</a>
    </nav>
    <div class="header-right">
      <a href="{root}about.html" style="color:white;font-size:.85rem;text-decoration:none;font-weight:600;">소개</a>
    </div>
  </div>
</header>

<script src="{root}js/wooa-sites-bar.js"></script>
<script src="{root}js/ad-dev-placeholder.js"></script>
"""

MOBILE_AD = """<div class="mobile-top-ad">
  <ins class="adsbygoogle" style="display:block;width:100%;min-height:60px"
    data-ad-client="ca-pub-6464921081676309"
    data-ad-slot="7080296704"
    data-ad-format="auto"
    data-full-width-responsive="true"></ins>
  <script>(adsbygoogle=window.adsbygoogle||[]).push({});</script>
</div>"""

MID_AD = """<div style="margin:24px 0;">
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6464921081676309" data-ad-slot="7080296704" data-ad-format="auto" data-full-width-responsive="true"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script>
</div>"""


def page_head(title, desc, keywords, canonical, root, extra_ld=""):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
{HEAD_COMMON}
  <meta name="google-site-verification" content="tNM8tmr_6DFold03YSScWz4KEtu5Zo0Fsqc03u5Afms" />
  <meta name="naver-site-verification" content="d77b9577794856d6f094b47de4a9017bfb9bb8ec" />
  <link rel="icon" href="{root}icons/icon.svg" type="image/svg+xml">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:image" content="{BASE_URL}/og-image.png">
  <meta property="og:site_name" content="WooaCert">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
{extra_ld}
  <link rel="manifest" href="{root}manifest.json">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-title" content="WooaCert">
  <link rel="stylesheet" href="{root}css/style.css">
</head>
"""


def gen_cert_page(cert):
    cat_id, cat_name, cat_color, cat_desc = CAT_MAP[cert["cat"]]
    canonical = f"{BASE_URL}/cert/{cert['slug']}.html"

    faq_ld = ",\n      ".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (json.dumps(q, ensure_ascii=False), json.dumps(a, ensure_ascii=False))
        for q, a in cert["faqs"]
    )
    extra_ld = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "name": {json.dumps(cert['name'], ensure_ascii=False)},
    "headline": {json.dumps(cert['title'], ensure_ascii=False)},
    "description": {json.dumps(cert['desc'], ensure_ascii=False)},
    "url": "{canonical}",
    "publisher": {{"@type": "Organization", "name": "WooaCert", "url": "{BASE_URL}"}},
    "inLanguage": "ko"
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_ld}
    ]
  }}
  </script>"""

    docs_html = "".join(f"<li>{d}</li>" for d in cert["docs"])
    uses_html = "".join(f"<li>{u}</li>" for u in cert["uses"])
    tips_html = "".join(f"<li>{t}</li>" for t in cert["tips"])
    faq_html = "".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in cert["faqs"]
    )

    online_badge = "🟢 온라인 발급 가능" if cert["online"] else "🔴 방문 발급만 가능"

    notice_html = ""
    if cert.get("notice"):
        notice_html = f'<div class="notice-box">⚠️ {cert["notice"]}</div>'

    online_cta_html = ""
    if cert["online"] and cert["slug"] in ONLINE_SITES:
        site_name, site_url = ONLINE_SITES[cert["slug"]]
        online_cta_html = f"""<div class="download-trigger-wrap">
    <a href="{site_url}" class="btn-download-main" style="text-decoration:none;">🔗 {site_name}에서 발급하러 가기</a>
  </div>"""

    body = f"""<div class="form-hero">
  <span class="cat-badge">{cat_name}</span>
  <h1>{cert['emoji']} {cert['name']}</h1>
  <p>{online_badge} · 발급기관: {cert['issuing_org']}</p>
</div>

<div class="page-with-sidebar">
<div class="form-content">

  <div class="breadcrumb">
    <a href="../index.html">홈</a> &rsaquo; <a href="../index.html#{cat_id}">{cat_name}</a> &rsaquo; {cert['name']}
  </div>

  <div class="info-grid">
    <div class="info-card"><div class="label">발급기관</div><div class="value">{cert['issuing_org']}</div></div>
    <div class="info-card"><div class="label">온라인 발급</div><div class="value">{'가능' if cert['online'] else '불가(방문 필수)'}</div></div>
    <div class="info-card"><div class="label">수수료(온라인)</div><div class="value">{cert['fee_online']}</div></div>
    <div class="info-card"><div class="label">수수료(방문)</div><div class="value">{cert['fee_offline']}</div></div>
  </div>

  {MID_AD}

  <p class="section-title">이 서류는 무엇인가요</p>
  <div class="desc-box">{cert['intro']}</div>

  {notice_html}

  <p class="section-title">💻 온라인 발급 방법</p>
  <div class="desc-box">{cert['online_desc']}</div>
  {online_cta_html}

  <p class="section-title">🏢 방문 발급 방법</p>
  <div class="desc-box">{cert['offline_desc']}</div>

  <p class="section-title">필요서류</p>
  <ul class="uses-list">{docs_html}</ul>

  <p class="section-title">주요 용도</p>
  <ul class="uses-list">{uses_html}</ul>

  <div class="info-grid" style="margin-top:20px;">
    <div class="info-card" style="grid-column:1/-1;"><div class="label">유효기간·참고</div><div class="value" style="font-weight:500;">{cert['validity']}</div></div>
  </div>

  <div class="wooa-orig-anchor"></div>

  <div class="tips-panel">
    <h3>💡 Tips</h3>
    <ul>{tips_html}</ul>
  </div>

  <div class="faq-section">
    <h2>자주 묻는 질문</h2>
    {faq_html}
    <details>
      <summary>이 사이트에서 실제로 {cert['name']}를 발급받을 수 있나요?</summary>
      <p>아니요. WooaCert는 발급 방법·절차 안내만 제공하며, 실제 발급은 위에서 안내한 공식 사이트({cert['issuing_org']}) 또는 방문 기관에서 진행하셔야 합니다. {kakao_naver_style_notice()}</p>
    </details>
  </div>

</div>
<aside class="tool-sidebar"></aside>
</div>

<footer class="footer"></footer>

<script src="../js/wooahouse-originals-tool.js"></script>
<script src="../js/wooa-sidebar.js"></script>
<script src="../js/wooa-footer.js"></script>
</body>
</html>
"""
    head = page_head(cert["title"] + " | WooaCert", cert["desc"], cert["keywords"], canonical, "../", extra_ld)
    html = head + "<body>\n\n" + HEADER_TMPL.format(root="../") + "\n" + body
    return html


def gen_index():
    cat_blocks = []
    for cat_id, cat_name, cat_color, cat_desc in CATEGORIES:
        certs = [c for c in CERTS if c["cat"] == cat_id]
        if not certs:
            continue
        cards = "".join(
            f"""<a href="cert/{c['slug']}.html" class="form-card">
          <span class="form-badge {'badge-free' if c['online'] else 'badge-ext'}">{'온라인가능' if c['online'] else '방문필수'}</span>
          <span class="form-icon">{c['emoji']}</span>
          <div class="form-name">{c['name']}</div>
          <div class="form-desc">{c['issuing_org']}</div>
          <span class="form-hint">자세히 보기 →</span>
        </a>"""
            for c in certs
        )
        cat_blocks.append(f"""
  <div class="category-block" id="{cat_id}">
    <div class="category-header">
      <div class="category-dot" style="background:{cat_color};"></div>
      <div>
        <h2 class="category-title">{cat_name}</h2>
        <p class="category-desc">{cat_desc}</p>
      </div>
    </div>
    <div class="forms-grid">
      {cards}
    </div>
  </div>""")

    item_list = ",\n      ".join(
        '{"@type":"ListItem","position":%d,"name":%s,"url":"%s/cert/%s.html"}' % (i + 1, json.dumps(c["name"], ensure_ascii=False), BASE_URL, c["slug"])
        for i, c in enumerate(CERTS)
    )
    extra_ld = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "WooaCert",
    "alternateName": ["우아서트", "증명서 발급 안내"],
    "url": "{BASE_URL}/",
    "description": "가족관계증명서·인감증명서·건강보험자격득실확인서 등 자주 필요한 증명서를 어디서 어떻게 발급받는지 정리한 안내 사이트",
    "inLanguage": "ko"
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "증명서 발급 안내 목록",
    "numberOfItems": {len(CERTS)},
    "itemListElement": [
      {item_list}
    ]
  }}
  </script>"""

    nav_tags = "".join(f'<a href="#{c[0]}" class="hero-tag">{c[1]}</a>' for c in CATEGORIES if any(x["cat"] == c[0] for x in CERTS))

    title = "증명서 발급 안내 — 어디서 어떻게 발급받나요 | WooaCert"
    desc = "가족관계증명서·인감증명서·건강보험자격득실확인서·범죄경력회보서 등 자주 필요한 증명서를 온라인으로 발급받을 수 있는지, 어디서 받는지, 수수료는 얼마인지 한눈에 정리했습니다."
    keywords = "증명서 발급, 증명서 인터넷발급, 정부24, 민원서류 발급, 증명서 발급처"

    body = f"""<section class="hero">
  <h1>어떤 증명서를, 어디서 발급받나요?</h1>
  <p>자주 필요한 증명서 {len(CERTS)}종의 온라인/방문 발급 방법과 수수료를 한곳에 정리했습니다.</p>
  <div class="hero-tags">{nav_tags}</div>
</section>

<div class="index-with-sidebar">
<div class="tools-section">
{''.join(cat_blocks)}
</div>
<aside class="index-sidebar"></aside>
</div>

<footer class="footer"></footer>

<script src="js/wooa-sidebar.js"></script>
<script src="js/wooa-footer.js"></script>
</body>
</html>
"""
    head = page_head(title, desc, keywords, f"{BASE_URL}/", "", extra_ld)
    html = head + "<body>\n\n" + HEADER_TMPL.format(root="") + "\n" + MOBILE_AD + "\n\n" + body
    return html


def gen_sitemap():
    urls = [f"  <url><loc>{BASE_URL}/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>"]
    for c in CERTS:
        urls.append(f"  <url><loc>{BASE_URL}/cert/{c['slug']}.html</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>")
    urls.append(f"  <url><loc>{BASE_URL}/about.html</loc><changefreq>yearly</changefreq><priority>0.3</priority></url>")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")


def main():
    CERT_DIR.mkdir(parents=True, exist_ok=True)
    for cert in CERTS:
        (CERT_DIR / f"{cert['slug']}.html").write_text(gen_cert_page(cert), encoding="utf-8")
    (ROOT / "index.html").write_text(gen_index(), encoding="utf-8")
    gen_sitemap()
    print(f"{len(CERTS)}개 증명서 페이지 + index + sitemap 생성 완료")


if __name__ == "__main__":
    main()

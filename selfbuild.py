from translator.basetranslator import basetrans
import requests
import re

class TS(basetrans):
    def langmap(self):
        """
        تحويل رموز اللغات الداخلية إلى الرموز التي يفهمها الخادم المحلي.
        """
        return {
            "Arabic": "ar",
            "English": "en",
            "French": "fr",
            "German": "de",
            "Spanish": "es",
            "Italian": "it",
            "Portuguese": "pt",
            "Russian": "ru",
            "Chinese": "zh-CN",
            "Korean": "ko",
            "Japanese": "ja",
            # أضف المزيد حسب الحاجة
        }

    def translate(self, query):
        api_url = "http://127.0.0.1:8000/translate"
        
        # الحصول على رموز اللغات الصحيحة
        source_lang = self.langmap().get(self.srclang, self.srclang)
        target_lang = self.langmap().get(self.tgtlang, self.tgtlang)
        unified_query = query.replace('\n', ' ').replace('\r', ' ').strip()
        # إعداد البيانات لإرسال النص كاملاً في طلب واحد
        payload = {
            "text": unified_query,
            "source": source_lang,
            "target": target_lang
        }
        
        # إرسال طلب POST
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            # إرجاع الترجمة مباشرة
            return response.json().get("translation", unified_query)
        else:
            # إذا فشلت الترجمة، أرجع النص الأصلي
            return unified_query


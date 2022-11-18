from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "content",
            "grade",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control mt-2",
                    "placeholder": "상품이 어떠셨나요? 솔직한 리뷰를 남겨 주세요^^",
                }
            ),
        }
        labels = {
            "content": "내용",
            "grade": "평점",
        }

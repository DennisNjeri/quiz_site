  @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(chartView, self)\
            .dispatch(request, *args, **kwargs)
    def displaydata(self,**kwargs):
        userprogress= Progress.objects.filter(user=self.request.user)
        pass
    def get_context_data(self, **kwargs):
        context = super(chartView, self).get_context_data(**kwargs)
        chart, c = Progress.objects.get_or_create(user=self.request.user)
        context['cat_scores'] = chart.list_all_cat_scores
        context['exams'] = chart.show_exams()
        return context



         context = super(chartView, self).get_context_data(**kwargs)
        chart, c = Progress.objects.get_or_create(user=self.request.user)
        context['cat_scores'] = chart.list_all_cat_scores
        context['exams'] = chart.show_exams()



        11,7,,9,11,,6,5,11,,8,,12,11,,8,,5,5,9,,7,,11,

        ['11', '7', '', '9', '11', '', '6', '5', '11', '', '8', '', '12', '11', '', '8', '', '5', '5', '9', '', '7', '', '11', '']
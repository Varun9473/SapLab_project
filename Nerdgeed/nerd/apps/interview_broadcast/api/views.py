# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from apps.interview_broadcast.models import dashbooard
# from apps.interview_broadcast.api.serializers import (
#         dashSerializer,
#     )

# from django.http import JsonResponse

# class InterviewList(APIView):

#     def get(self, request, format=None):
#         contents_snippets = dashbooard.objects.all()
#         serializer = dashSerializer(contents_snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         # serializer = JobSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         print(request.data)
#         return JsonResponse({'status': 'ok'})


# class contentDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404


#     def get(self, request, pk, format=None):
#         contents_snippets = self.get_object(pk)
#         serializer = CategorySerializer(contents_snippets)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#        contents_snippets = self.get_object(pk)
#        serializer = CategorySerializer(contents_snippets, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         contents_snippets = self.get_object(pk)
#         contents_snippets.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
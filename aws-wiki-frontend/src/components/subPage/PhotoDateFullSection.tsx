import React, { useState } from "react";
import { getPhotoDateList } from "../action";
import useSWR from "swr";
import { Card, Image, useDisclosure } from "@nextui-org/react";
import { FormatDate } from "@/utils/FormatDate";
import { IPhoto } from "@/utils/DataType";
import PhotoModal from "../bigModal/PhotoModal";

interface IPhotoDate {
  searchDate: string;
}

const PhotoDateFullSection = ({ searchDate }: IPhotoDate) => {
  const [selectedPhoto, setSelectedPhoto] = useState<IPhoto | null>(null);
  const { isOpen, onOpen, onOpenChange } = useDisclosure();

  const {
    data: photoList,
    error,
    isLoading,
  } = useSWR(searchDate, (searchDate) => getPhotoDateList(searchDate));
  if (isLoading) return <p>이미지를 가져오는 중입니다! 잠시만 기다려주세요</p>;
  if (error) return <p>이미지가 없습니다.</p>;

  const handleCardClick = (photo: IPhoto) => {
    setSelectedPhoto(photo);
    onOpen();
  };

  return (
    <div>
      <div className="grid grid-cols-3 gap-4">
        {photoList.map((photo: IPhoto) => (
          <Card
            key={photo.index}
            className="p-4 border-3 border-blue-400 hover:shadow-xl hover:border-purple-500"
            shadow="none"
            isPressable
            onPress={() => handleCardClick(photo)}
          >
            <div className="font-bold text-lg mb-2">
              {FormatDate(photo.date)}
            </div>
            <Image src={photo.image} width={500} height={250} alt="사진" />
          </Card>
        ))}
      </div>
      {selectedPhoto && (
        <PhotoModal
          isOpen={isOpen}
          onOpen={onOpen}
          onOpenChange={onOpenChange}
          data={selectedPhoto}
        />
      )}
    </div>
  );
};

export default PhotoDateFullSection;
